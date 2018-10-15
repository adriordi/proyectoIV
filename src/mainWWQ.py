

class WorkWaitQueue:
    
    def __init__(self, name, nw):
        self._name = name
        self._nWorks = nw

    def name(self):
        return self._name

    def nWorks(self):
        return self._nWorks
        
    def addnWorks(self):
        self._nWorks += 1

    def delnWorks(self):
        if self._nWorks >= 1:
            self._nWorks -= 1
        else:
            print("La cola esta vacia")
        
    def queueEmpty(self):
        if self._nWorks == 0:
            return True
        else:
            return False
