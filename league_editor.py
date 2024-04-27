import csv
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
from team import Team
from team_editor import MainWindow3

Ui_MainWindow2, QtBaseWindow = uic.loadUiType('league_editor.ui')


class MainWindow2(QtBaseWindow, Ui_MainWindow2):
    def __init__(self, currentDB, currentLeague, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.currentLeague = currentLeague
        self.currentDB = currentDB
        self.add_pushButton.clicked.connect(self.addTeam_pushButton_clicked)
        self.edit_pushButton.clicked.connect(self.editTeam_pushButton_clicked)
        self.delete_pushButton.clicked.connect(self.deleteTeam_pushButton_clicked)
        self.import_pushButton.clicked.connect(self.importTeam_pushButton_clicked)
        self.export_pushButton.clicked.connect(self.exportTeam_pushButton_clicked)

    def addTeam_pushButton_clicked(self):
        if self.lineEdit.text() != '':
            newTeam = Team(self.currentDB.next_oid(), self.lineEdit.text())
            self.currentLeague.add_team(newTeam)
            print(self.currentLeague.teams)
            self.listWidget.addItem(newTeam.name)
            self.lineEdit.clear()
        else:
            raise Exception('No team name entered')

    def editTeam_pushButton_clicked(self):
        if self.listWidget.currentRow() >= 0:
            currentTeam = self.listWidget.currentItem()
            currentTeam = currentTeam.text()
            currentTeam = self.currentLeague.team_named(currentTeam)
            self.window3 = MainWindow3(self.currentDB, self.currentLeague.teams[self.listWidget.currentRow()], currentTeam)
            for member in currentTeam.members:
                self.window3.listWidget.addItem(f'{member.name}')
            self.window3.show()
        else:
            raise Exception('No team selected for editing')
    def deleteTeam_pushButton_clicked(self):
        if self.listWidget.currentRow() >= 0:
            currentTeam = self.listWidget.currentItem()
            currentTeam = currentTeam.text()
            currentTeam = self.currentLeague.team_named(currentTeam)
            self.currentLeague.remove_team(currentTeam)
            self.listWidget.takeItem(self.listWidget.currentRow())
        else:
            raise Exception('No team selected for deletion')

    def importTeam_pushButton_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File')
        reader = csv.reader(open(filename[0], 'r'))
        for row in reader:
            team = Team(self.currentDB.next_oid(), row[0])
            self.currentLeague.add_team(team)
            self.listWidget.addItem(team.name)
        for team in self.currentLeague.teams:
            print(team.name)
            print(team.oid)

    def exportTeam_pushButton_clicked(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File')
        writer = csv.writer(open(filename[0], 'w'))
        for team in self.currentLeague.teams:
            writer.writerow([team.name])






