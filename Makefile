install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	ruff check *.py 
	
test:
	python -m pytest -vv tests/test_*.py 

check:
	python main.py
	git config --local user.email "action@github.com"; \
	git config --local user.name "Github Action"; \
	git add .; \
	git commit -m "test"; \
	git push; \

deploy:
	#deploy goes here

all: install lint format test 

