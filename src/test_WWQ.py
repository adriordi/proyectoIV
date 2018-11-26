import unittest
import json
import requests
from src.mainWWQ import WorkWaitQueue

url = "https://workwaitqueue.herokuapp.com/"

def test_status(self):
    response = requests.get(url)
    self.assertEqual(self.response.status,200)

def test_works(self):
    response = requests.get(url+"works")
    self.assertEqual(self.response.status,200)

def test_empty(self):
    response = requests.get(url+"empty")
    self.assertEqual(self.response.status,200)

class testWWQ(unittest.TestCase):
    def setUp(self):
        self.queue = WorkWaitQueue("cola1", 0)

    def test_queue_is_empty(self):
        self.assertEqual(self.queue.queueEmpty(),True,"La cola esta vacia")

    def test_increment_works(self):
        # This avoid hardcode the number of jobs in the assert
        previous_size = self.queue.size()
        self.queue.addnWorks()
        self.assertEqual(self.queue.size(), previous_size + 1)

    def test_decrement_works(self):
        # This avoid hardcode the number of jobs in the assert
        previous_size = self.queue.size()
        final_size = 0 if previous_size is 0 else previous_size - 1
        self.queue.delnWorks()
        self.assertEqual(self.queue.size(), final_size)

    def test_decrement_works_non_null(self):
        # Add some works
        self.queue.addnWorks()
        self.queue.addnWorks()
        # This avoid hardcode the number of jobs in the assert
        previous_size = self.queue.size()
        final_size = 0 if previous_size is 0 else previous_size - 1
        self.queue.delnWorks()
        self.assertEqual(self.queue.size(), final_size)

if __name__ == '__main__':
    unittest.main()
