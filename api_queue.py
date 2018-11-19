import hug
import json

from src.mainWWQ import WorkWaitQueue

queue = WorkWaitQueue("service_queue", 0)

@hug.get('/')
def status():
        """Returns json with app status"""
        response = {
                "status": "OK",
        }
        
        return response
        
@hug.get()
def get_works():
	""" Returns json containing the size of the queue"""
	response = {
		"status": 200,
		"description": "OK",
		"data": {
			"queue size": queue.size()
		}
	}

	return response

@hug.post("/add_work")
def add_work(body=None):
	"""Adds a new job to the queue"""
	try:
		queue.addnWorks()
		status = 200
		description = "OK"
	except Exception as e:
		status = 500
		description = "Error: Internal server error"

	response = {
		"status": status,
		"description": description
	}

	return response
