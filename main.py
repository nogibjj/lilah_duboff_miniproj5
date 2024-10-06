# calls all the extract, transform, query functions to main
"""
ETL-Query script
"""

from SQL_files.extract import extract_data
from SQL_files.transform import transform
from SQL_files.query import read, update, delete, query_1, query_2

database = "remotehealthDB.db"
table = "remotehealthDB"
url = "https://raw.githubusercontent.com/lilah-duboff/data-for-URLS/refs/heads/main/Impact_of_Remote_Work_on_Mental_Health.csv"
path = "data/remote_work_mental_health_data.csv"
folder = "data"


def main():
    # Extract
    print("Extracting data...")
    extract_data(url, path, folder)

    # Transform and load/create
    print("Transforming data...")
    transform(path)

    # CRUD
    read(database, table)
    update(database, table, "Age", 35, "EMP0040")
    delete(database, table, "EMP0040")

    # Query
    print("First query...")
    print(query_1())
    print("Second query...")
    print(query_2())


if __name__ == "__main__":
    main()
