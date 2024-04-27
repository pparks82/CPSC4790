import keyring
import yagmail

class Emailer:
    sender_address = ""
    _sole_instance = None

    def configure(self, sender_address):
        sender_address = sender_address
    
    def instance():
        _sole_instance = Emailer()
        return _sole_instance
    def send_plain_email(self, recipients, subject, message):
        self.recipients = recipients
        self.subject = subject
        self.message = message
        keyring.set_password('gmail', 'patrick.parks.157@gmail.com')
        yag = yagmail.SMTP(user='patrick.parks.157@gmail.com')
        for recipient in recipients:
            yag.send(recipient, self.subject, self.message)