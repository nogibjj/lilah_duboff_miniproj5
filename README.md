[![Python Application Test with Github Actions](https://github.com/lilah-duboff/scaffold/actions/workflows/main.yml/badge.svg)](https://github.com/lilah-duboff/scaffold/actions/workflows/main.yml)

# Python Script interacting with SQL Database
#### This project imports a csv dataset, converts it to a database, and performs CRUD operations to analyze data

#### Requirements:

- [X] Connect to a SQL database
- [X] Perform CRUD operations
- [X] Write at least two different SQL queries
- [X] Database connection
- [X] CRUD operations
- [X] CI/CD pipeline
- [X] Test each operation works by loading the .db file into your pipeline 
- [X] README.md
- [X] Screenshot or log of successful database operations
- [X] Arch Diagram
- [X] CLI - BONUS 

---
### Folder Navigation
##### Here is a quick overview of how the folders are structured for this project:
---
- Project Folder
    - .devcontainer
        - devcontainer.json
        - Dockerfile
    - .github
        - workflows
            - main.yml
    - data
        - data csv file (optional to import into the folder, could use URL)
    - main_files
        - main.py
        - test_main.py
    - SQL_files
        - extract.py
        - query.py
        - transform.py
    - Makefile
    - README.md
    - remote_work_mental_health.db (database created from csv)
    - requirements.txt
---
### Workflow Summary and Explanation
##### This project contains the following dependencies:
- pylint
- black 
- pytest
- ruff 
- sqlite3
- fire

---
### Arch Diagram and Explanation
