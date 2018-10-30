class WorkWaitQueue:

    def __init__(self, name, nw):
        self._name = name
        self._nWorks = nw

    def name(self):
        return self._name

    def size(self):
        return self._nWorks

    def nWorks(self):
        """
        Returns the number of works waiting to be proccesseds.
        """
        return self._nWorks

    def addnWorks(self):
        """
        Increments the number of works waiting in the queue.
        """
        self._nWorks += 1

    def delnWorks(self):
        """
        Decrements (if possible) the numbers of works waiting
        in the queue
        """
        if self._nWorks >= 1:
            self._nWorks -= 1
        else:
            print("La cola esta vacia")

    def queueEmpty(self):
        """
        Returns wether the queue is empty or not.
        """
        if self._nWorks == 0:
            return True
        else:
            return False
