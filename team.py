# team.py #
# Patrick Parks #
# Auburn University #
# CPSC 4790 #
# 3/24/24 #

from identified_object import IdentifiedObject
from exceptions import DuplicateEmail, DuplicateOid

class Team(IdentifiedObject):
    
    @property
    def members(self):
        return self._members
    
    def __init__(self, oid, name):
        super().__init__(oid)
        self.name = name
        self._members = []
    
    def add_member(self, member):
        if member in self._members:
            raise DuplicateOid("Member already exists")
        else:
            self._members.append(member)

    def member_named(self, s):
        for member in self._members:
            if member.name == s:
                return member
    
    def remove_member(self, member):
        if member in self._members:
            self._members.remove(member)
    
    def send_email(self, emailer, subject, message):
        recipients = []
        for member in self._members:
            recipients.append(member.email)
        self.emailer = emailer
        self.subject = subject
        self.message = message
        for member in self._members:
            emailer.send_plain_email(recipients, self.subject, self.message)

    def __str__(self):
        print(f"Team Name: {self.name} {len(self.members)} members")
        
    