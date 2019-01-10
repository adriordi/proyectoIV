class WorkWaitQueue:

    def __init__(self, name, nw, npw):
        self._name = name
        self._nWorks = nw
        self._nPriorityWorks = npw

    def name(self):
        """
        Returns the name of the queue
        """
        return self._name

    def nWorks(self):
        """
        Returns the number of works waiting to be proccesseds.
        """
        return self._nWorks

    def nPriorityWorks(self):
        """
        Returns the number of works with priority in queue.
        """
        return self._nPriorityWorks
        
    def addWork(self):
        """
        Increments the number of works waiting in the queue.
        """
        self._nWorks += 1

    def addPriorityWork(self):
        """
        Adds work and incrementes the number of works with priority.
        """
        self.addWork()
        self._nPriorityWorks += 1
        
    def delWork(self):
        """
        Decrements (if possible) the numbers of works waiting
        in the queue
        """
        if self._nWorks >= 1:
            self._nWorks -= 1
        else:
            print("La cola esta vacia")

    def delPriorityWork(self):
        """
        Decrements the number of works with priority
        """
        if self._nPriorityWorks >=1:
            self.delWork()
            self._nPriorityWorks -= 1
        else:
            print("No hay trabajos con prioridad.")
        

    def queueEmpty(self):
        """
        Returns whether the queue is empty or not.
        """
        if self._nWorks == 0:
            return True
        else:
            return False

    
