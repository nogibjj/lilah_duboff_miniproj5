"""asserts if data exists, if a database was created
and if the CRUD operations returned a result"""

from SQL_files.query import read, update, delete, query_1, query_2
import sqlite3



def test_read():
    result = read("remotehealthDb.db", "remotehealthDB")

    assert isinstance(result, list)
    assert len(result) > 0

# data, table, column, new_value, ID_number
def test_update():
    ID_number = "EMP0001"
    column = "Age"
    new_value = "EMP0000"

    result = update("remotehealthDB.db", "remotehealthDB", column, new_value, ID_number)
    assert result == "Record updated successfully!"

def test_delete():

    ID_number = "EMP0008"
    result = delete("remotehealthDB.db", "remotehealthDB", ID_number)

    assert result == "Record deleted successfully!"


def test_query_1():
    result_1 = query_1()
    assert result_1 is not None


def test_query_2():
    result_2 = query_2()
    assert result_2 is not None


if __name__ == "__main__":
    test_read()
    test_update()
    test_delete()
    test_query_1()
    test_query_2()
