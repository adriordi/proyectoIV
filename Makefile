install:
	pip3 install -r requirements.txt

test:
#	docker run <docker> -p 8000
	python3 -m pytest src
