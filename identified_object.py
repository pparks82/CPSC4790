# identified_object.py #
# Patrick Parks #
# Auburn University #
# CPSC 4790 #
# 3/24/24 #

class IdentifiedObject:
    
    @property
    def oid(self):
        return self._oid
    
    def __init__(self, oid):
        self._oid = oid
    
    def __eq__(self, other):
        return(type(self) == type(other) and self.oid == other.oid)
    
    def __hash__(self):
        return hash(self.oid)