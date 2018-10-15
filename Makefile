install:
	pip3 install -r requeriments.txt

test:
	cd ./src/ && python3 test_Status.py
