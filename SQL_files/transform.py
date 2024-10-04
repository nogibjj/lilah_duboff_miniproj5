# This file should take the cvs data and convert it into a database, or .db file
import sqlite3
import csv
import sys

data = "data/Impact_of_Remote_Work_on_Mental_Health.csv"


def transform():
    """ "Transforms and Loads data into the local SQLite3 database"""
    payload = csv.reader(open(data, newline=""), delimiter=",")
    next(payload)
    conn = sqlite3.connect("remotehealthDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS remotehealthDB")
    c.execute(
        """
              CREATE TABLE remotehealthDB (
                    Employee_ID,
                    Gender, 
                    Age,
                    Job_Role,
                    Industry,
                    Years_of_Experience,
                    Work_Location,
                    Hours_Worked_Per_Week,
                    Number_of_Virtual_Meetings,
                    Work_Life_Balance_Rating,
                    Stress_Level,
                    Mental_Health_Condition,
                    Access_to_Mental_Health_Resources,
                    Productivity_Change,
                    Social_Isolation_Rating,
                    Satisfaction_with_Remote_Work,
                    Company_Support_for_Remote_Work,
                    Physical_Activity,
                    Sleep_Quality,
                    Region 
                  )
              """
    )
    # insert
    c.executemany(
        """INSERT INTO remotehealthDB VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "remotehealthDB.db"
