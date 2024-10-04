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
https://private-user-images.githubusercontent.com/58792/271664601-b39b21b4-ccb4-4cc4-b262-7db34492c16d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjgwMDQ2MzMsIm5iZiI6MTcyODAwNDMzMywicGF0aCI6Ii81ODc5Mi8yNzE2NjQ2MDEtYjM5YjIxYjQtY2NiNC00Y2M0LWIyNjItN2RiMzQ0OTJjMTZkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDEwMDQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQxMDA0VDAxMTIxM1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTYyYWIyYzgxY2UzNTc2M2I2YTVhNjE1Y2QwODI0NTI3ZDc3YjBhNjg5ZmVkZDVmODVjY2M3OTIzMzI0YmMwNGYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.waBDd48fH-44j1ONqF0xrJyy35WQSdezIBH9eSVQ_BE