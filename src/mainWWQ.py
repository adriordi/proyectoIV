

class WorkWaitQueue:

    def __init__(self, name):
        self._name = name
        self._nWorks = 0

    def name(self):
        return self._name

    def nWorks(self):
        return self._nWorks
        
    def addnWorks(self):
        self.nWorks += 1

    def delnWorks(self):
        if nWorks >= 1:
            self.nWorks -= 1
        else:
            print("La cola esta vacia")
        
        
