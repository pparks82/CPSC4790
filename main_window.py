import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import league_database
from league_editor import MainWindow2
from league import League
from team import Team

Ui_MainWindow, QtBaseWindow = uic.loadUiType('main_window.ui')
db = league_database.LeagueDatabase.instance()


class MainWindow(QtBaseWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.load_pushButton.clicked.connect(self.load_button_clicked)
        self.add_pushButton.clicked.connect(self.add_pushButton_clicked)
        self.save_pushButton.clicked.connect(self.save_pushButton_clicked)
        self.edit_pushButton.clicked.connect(self.edit_pushButton_clicked)
        self.delete_pushButton.clicked.connect(self.delete_pushButton_clicked)

    def load_button_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')
        db.load(filename[0])
        for league in db.leagues:
            self.league_listWidget.addItem(league)

    def add_pushButton_clicked(self):
        if self.leagueName_lineEdit.text() != '':
            newLeague = League(db.next_oid, self.leagueName_lineEdit.text())
            db.add_league(newLeague)
            print(newLeague.name)
            print(newLeague.teams)
            self.league_listWidget.addItem(newLeague.name)
            print(db.leagues)
            self.leagueName_lineEdit.clear()
        else:
            raise Exception('No League Name')

    def save_pushButton_clicked(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')
        db.save(filename[0])

    def edit_pushButton_clicked(self):
        if self.league_listWidget.currentRow() >= 0:
            self.window2 = MainWindow2(db, db.leagues[self.league_listWidget.currentRow()])
            for team in db.leagues[self.league_listWidget.currentRow()].teams:
                self.window2.listWidget.addItem(team.name)
            self.window2.show()
        else:
            raise Exception('No League Selected for Editing')

    def delete_pushButton_clicked(self):
        if self.league_listWidget.currentRow() >= 0:
            league = self.league_listWidget.currentItem()
            row = self.league_listWidget.currentRow()
            db.remove_league(league.text())
            self.league_listWidget.takeItem(row)
            print(db.leagues)
        else:
            raise Exception('No League Selected for Deleting')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
