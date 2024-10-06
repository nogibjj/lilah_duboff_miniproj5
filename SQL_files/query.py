import sqlite3


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
    c.execute("SELECT * FROM remotehealthDB LIMIT 5")
    print("Top 5 rows of the remotehealthDB table:")
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
        "SELECT Job_Role, Industry, Hours_Worked_Per_Week, Stress_Level, Mental_Health_Condition FROM remotehealthDB WHERE Hours_Worked_Per_Week=(SELECT MAX(Hours_worked_per_week) FROM remotehealthDB)"
    )
    print("Max hours worked per week from remotehealthDB table:")
    query_2_result = c.fetchall()
    print("Query is complete!")
    conn.close()
    return query_2_result
