import csv
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
from team import Team
from team_member import TeamMember

Ui_MainWindow3, QtBaseWindow = uic.loadUiType('team_editor.ui')


class MainWindow3(QtBaseWindow, Ui_MainWindow3):
    def __init__(self, currentDB, currentLeague, currentTeam, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.currentLeague = currentLeague
        self.currentDB = currentDB
        self.currentTeam = currentTeam
        self.add_pushButton.clicked.connect(self.add_pushButton_clicked)
        self.delete_pushButton.clicked.connect(self.delete_pushButton_clicked)
        self.update_pushButton.clicked.connect(self.update_pushButton_clicked)

    def add_pushButton_clicked(self):
        newMember = TeamMember(self.currentDB.next_oid(), self.name_lineEdit.text(), self.email_lineEdit.text())
        self.currentTeam.add_member(newMember)
        self.listWidget.addItem(newMember.name)
        self.name_lineEdit.clear()
        self.email_lineEdit.clear()
        print(self.currentTeam.members)

    def delete_pushButton_clicked(self):
        currentRow = self.listWidget.currentItem()
        currentMemberName = currentRow.text()
        print(currentMemberName)
        currentMember = self.currentTeam.member_named(currentMemberName)
        self.currentTeam.remove_member(currentMember)
        print(self.currentTeam.members)
        self.listWidget.takeItem(self.listWidget.currentRow())

    def update_pushButton_clicked(self):
        currentMember = self.currentTeam.member_named(self.listWidget.currentItem().text())
        print(currentMember)
        currentMember.name = self.name_lineEdit_update.text()
        currentMember.email = self.email_lineEdit_update.text()
        self.listWidget.takeItem(self.listWidget.currentRow())
        self.listWidget.addItem(currentMember.name)
        print(currentMember)