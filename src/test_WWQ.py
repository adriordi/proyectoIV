import unittest
import json
import requests
from src.mainWWQ import WorkWaitQueue
from requests import *

# url = "https://workwaitqueue-docker.herokuapp.com/"
#url = "localhost:8000"

class testWWQ(unittest.TestCase):
    def setUp(self):
        self.queue = WorkWaitQueue("cola1", 0)

    def test_queue_is_empty(self):
        self.assertEqual(self.queue.queueEmpty(),True,"La cola esta vacia")

    def test_increment_works(self):
        # This avoid hardcode the number of jobs in the assert
        previous_size = self.queue.nWorks()
        self.queue.addWork()
        self.assertEqual(self.queue.nWorks(), previous_size + 1)

    def test_decrement_works(self):
        # This avoid hardcode the number of jobs in the assert
        previous_size = self.queue.nWorks()
        final_size = 0 if previous_size is 0 else previous_size - 1
        self.queue.delWork()
        self.assertEqual(self.queue.nWorks(), final_size)

    def test_decrement_works_non_null(self):
        # Add some works
        self.queue.addWork()
        self.queue.addWork()
        # This avoid hardcode the number of jobs in the assert
        previous_size = self.queue.nWorks()
        final_size = 0 if previous_size is 0 else previous_size - 1
        self.queue.delWork()
        self.assertEqual(self.queue.nWorks(), final_size)

#    def test_status(self):
#        r = requests.get(url)
#        self.assertEqual(r.status_code,200,"Devuelve status 200")

#    def test_works(self):
#        r = requests.get(url+"works")
#        self.assertEqual(r.status_code,200,"Devuelve status 200")

#    def test_empty(self):
#        r = requests.get(url+"empty")
#        self.assertEqual(r.status_code,200,"Devuelve status 200")

        
        
if __name__ == '__main__':
    unittest.main()
