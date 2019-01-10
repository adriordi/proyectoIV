import hug
import json
from src.mainWWQ import WorkWaitQueue

queue = WorkWaitQueue("service_queue", 0, 0)

@hug.get('/')
def status():
        """Returns json with app status"""
        response = {
                "status": "OK",
        }
        
        return response

@hug.get('/status')
def status():
        """Returns json with app status"""
        response = {
                "status": "OK",
        }
        
        return response
        
@hug.get()
def works():
	""" Returns json containing with the number of jobs that queue have"""
	response = {
		"status": 200,
		"description": "OK",
		"data": {
			"queue size": queue.nWorks()
		}
	}

	return response

@hug.put()
def add_work():
	"""Adds a new job to the queue"""
	try:
		queue.addWork()
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

@hug.put()
def del_work():
	"""Delete a job to the queue"""
	try:
		queue.delWork()
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

@hug.get()
def empty():
	""" Returns json with true or false according to queue is empty"""
	response = {
		"status": 200,
		"description": "OK",
		"data": {
			"queue empty": queue.queueEmpty()
		}
	}

	return response


