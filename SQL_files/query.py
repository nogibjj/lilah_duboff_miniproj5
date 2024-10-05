import sqlite3


def query_1():
    """queries the db for top five rows"""
    conn = sqlite3.connect("remotehealthDB.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM remotehealthDB LIMIT 5")
    print("Top 5 rows of the remotehealthDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"


def query_2():
    """queries the db for max hours worked per week,
    and collects the subsequent information"""
    conn = sqlite3.connect("remotehealthDB.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT Job_Role, Industry, Hours_Worked_Per_Week, Stress_Level, Mental_Health_Condition FROM remotehealthDB WHERE Hours_Worked_Per_Week=(SELECT MAX(Hours_worked_per_week) FROM remotehealthDB)"
    )
    print("Max hours worked per week from remotehealthDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"
