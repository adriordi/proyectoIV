import unittest
from mainWWQ import WorkWaitQueue

class testWWQ(unittest.TestCase):
    def setUp(self):
        self.queue = WorkWaitQueue("cola1", 0)

    def test_queue_is_empty(self):
        self.assertEqual(self.queue.queueEmpty(),True,"La cola esta vacia")


if __name__ == '__main__':
    unittest.main()
