class DuplicateOid(Exception):
    def __init__(self, message):
        super().__init__(message)

class DuplicateEmail(Exception):
    def __init__(self, message):
        super().__init__(message)