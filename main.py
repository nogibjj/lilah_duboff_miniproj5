# calls all the extract, transform, query functions to main
"""
ETL-Query script
"""

from SQL_files.extract import extract_data
from SQL_files.transform import transform
from SQL_files.query import query

# Extract
print("Extracting data...")
extract_data()

# Transform and load
print("Transforming data...")
transform()

# Query
print("Querying data...")
query()
