# competition.py #
# Patrick Parks #
# Auburn University #
# CPSC 4790 #
# 3/24/24 #

from identified_object import IdentifiedObject
import datetime
from exceptions import DuplicateEmail, DuplicateOid

class Competition(IdentifiedObject):

    def __init__(self, oid, teams, location, date_time):
        super().__init__(oid)
        if teams == []:
            self._teams_competing = []
        else:    
            self._teams_competing = [teams[0], teams[1]]
        self.location = location
        if date_time == None:
            self.date_time = None
        else:
            self.date_time = date_time
    
    @property
    def teams_competing(self):
        return self._teams_competing

    def location(self):
        return self.location

    def send_email(self, emailer, subject, message):
        recipients = []
        for team in self.teams_competing:
            for member in team.members:
                if member.email not in recipients:
                    recipients.append(member.email)
        self.emailer = emailer
        self.subject = subject
        self.message = message
        emailer.send_plain_email(recipients, self.subject, self.message)

    def __str__(self):
        if self.date_time == None:
            date = None
        else:
            date = self.date_time.strftime("%d/%M/%Y %H:%M")
        if date == None:
            print(f"Competition at {self.location} with {len(self.teams_competing)} teams")
        else:    
            print(f"Competition at {self.location} on {date} with {len(self.teams_competing)} teams")