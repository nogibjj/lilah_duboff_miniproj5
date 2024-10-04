install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black ./main_files

lint:
	ruff check ./main_files/*.py 
	
test:
	python -m pytest -vv ./main_files/test_*.py 

check:
	python ./main_files/main.py
	git config --local user.email "action@github.com"; \
	git config --local user.name "Github Action"; \
	git add .; \
	git commit -m "test"; \
	git push; \

deploy:
	#deploy goes here

all: install lint format test 

extract:
	python main.py extract

transform_load: 
	python main.py transform_load

query:
	# using delete query as an example
	python main.py delete_record 10