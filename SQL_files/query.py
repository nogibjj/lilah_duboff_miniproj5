import sqlite3


def create(data, table):
    conn = sqlite3.connect(data)
    cursor = conn.cursor()
    cursor.execute(
        f"""CREATE TABLE IF NOT EXISTS {table} 
                    (Employee_ID TEXT,
                    Gender TEXT, 
                    Age INTEGER,
                    Job_Role TEXT,
                    Industry TEXT,
                    Years_of_Experience INTEGER,
                    Work_Location TEXT,
                    Hours_Worked_Per_Week INTEGER,
                    Number_of_Virtual_Meetings INTEGER,
                    Work_Life_Balance_Rating INTEGER,
                    Stress_Level INTEGER,
                    Mental_Health_Condition TEXT,
                    Access_to_Mental_Health_Resources TEXT,
                    Productivity_Change TEXT,
                    Social_Isolation_Rating INTEGER,
                    Satisfaction_with_Remote_Work INTEGER,
                    Company_Support_for_Remote_Work TEXT,
                    Physical_Activity INTEGER,
                    Sleep_Quality INTEGER,
                    Region TEXT 
                  )"""
    )

    query = f"INSERT INTO {table} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    cursor.execute(query, data)
    conn.commit()
    if len(data) != 20:
        raise ValueError(f"Expected 20 values for insertion, got {len(data)}.")
    conn.close()
    return table


def read(data, table):
    conn = sqlite3.connect(data)
    c = conn.cursor()
    query = f"SELECT * FROM {table}"
    c.execute(query)
    read_result = c.fetchall()
    c.close()
    conn.close()

    return read_result


def update(data, table, column, new_value, ID_number):
    """Update a specific column in a row based on Employee_ID"""
    conn = sqlite3.connect(data)
    c = conn.cursor()
    query = f"UPDATE {table} SET {column} = ? WHERE Employee_ID = ?"
    c.execute(query, (new_value, ID_number))
    affected_rows = c.rowcount
    conn.commit()
    c.close()
    conn.close()

    if affected_rows == 0:
        print("No record found")
        return "No record found"
    print("Record updated successfully!")
    return "Record updated successfully!"


def delete(database, table, ID_number):
    conn = sqlite3.connect(database)
    c = conn.cursor()
    query = f"DELETE FROM {table} WHERE Employee_ID = ?"
    c.execute(query, (ID_number,))
    changed_rows = c.rowcount
    conn.commit()
    c.close()
    conn.close()

    if changed_rows == 0:
        print("No record found")
        return "No record found"
    print("Record deleted successfully!")
    return "Record deleted successfully!"


def query_1():
    """queries the db for top five rows"""
    conn = sqlite3.connect("remotehealthDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM remote_health LIMIT 5")
    print("Top 5 rows of the remote_health table:")
    query_1_result = c.fetchall()
    print("Query is complete")
    conn.close()
    return query_1_result


def query_2():
    """queries the db for max hours worked per week,
    and collects the subsequent information"""
    conn = sqlite3.connect("remotehealthDB.db")
    c = conn.cursor()
    c.execute(
        "SELECT Job_Role, Industry, Hours_Worked_Per_Week, Stress_Level, Mental_Health_Condition FROM remote_health WHERE Hours_Worked_Per_Week=(SELECT MAX(Hours_worked_per_week) FROM remote_health)"
    )
    print("Max hours worked per week from remote_health table:")
    query_2_result = c.fetchall()
    print("Query is complete!")
    conn.close()
    return query_2_result
