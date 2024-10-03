# This file should take the cvs data and convert it into a database, or .db file
import sqlite3
import csv

data = "data/Impact_of_Remote_Work_on_Mental_Health.csv"


# load the csv file and insert into a new sqlite3 database
def transform(data):
    """ "Transforms and Loads data into the local SQLite3 database"""
    # prints the full working directory and path
    # print(os.getcwd())
    payload = csv.reader(open(data, newline=""), delimiter=",")
    next(payload)
    conn = sqlite3.connect("remote_work_and_mental_health.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS remotehealthDB")
    c.execute(
        """
              CREATE TABLE remotehealthDB (
                    Employee_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Gender TEXT, 
                    Age INTEGER,
                    Job_Role TEXT,
                    Industry TEXT,
                    Years_of_Experience INTEGER,
                    Work_Location TEXT,
                    Hours_Worked_Per_Week INTEGER,
                    Number_of_Virtual_Meetings INTEGER,
                    Work_Life_Balance_Rating INTEGER,
                    Stress_Level TEXT,
                    Mental_Health_Condition TEXT,
                    Access_to_Mental_Health_Resources TEXT,
                    Productivity_Change TEXT,
                    Social_Isolation_Rating INTEGER,
                    Satisfaction_with_Remote_Work TEXT,
                    Company_Support_for_Remote_Work INTEGER,
                    Physical_Activity TEXT,
                    Sleep_Quality TEXT,
                    Region TEXT
                  )
              """
    )
    # insert
    c.executemany(
        """
                  INSERT INTO remotehealthlDB (
                        Age, 
                        Years_of_Experience,
                        Number_of_Virtual_Meetings,
                        Social_Isolation_Rating,
                        Company_Support_for_Remote_Work,
                        Satisfaction_with_Remote_Work,
                        Industry,
                        Mental_Health_Condition,
                        Access_to_Mental_Health_Resources
                      ) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                  """,
        payload,
    )
    conn.commit()
    conn.close()
    return "remotehealthDB.db"
