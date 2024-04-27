# team_member.py #
# Patrick Parks #
# Auburn University #
# CPSC 4790 #
# 3/24/24 #

from identified_object import IdentifiedObject

class TeamMember(IdentifiedObject):

    def __init__(self, oid, name, email):
        super().__init__(oid)
        self.name = name
        self.email = email

    def send_email(self, emailer, subject, message):
        self.emailer = emailer
        self.recipients = self.email
        self.subject = subject
        self.message = message
        emailer.send_plain_email([self.recipients], self.subject, self.message)

    def __str__(self):
        return(f"{self.name}<{self.email}>")
    