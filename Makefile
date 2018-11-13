install:
	pip3 install -r requirements.txt

test:
	cd ./src/ && python3 test_WWQ.py
