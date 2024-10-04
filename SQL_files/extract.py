# can use this file to extract csv from a url
""" This file can take csv data from a url and extract it to be transformed and queried """

import requests
import os


def extract_data():
    """Extract data from a url to a file path"""
    url = "https://github.com/lilah-duboff/data-for-URLS/blob/main/Impact_of_Remote_Work_on_Mental_Health.csv"
    path = "data/remote_work_mental_health_data.csv"
    directory = "data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(path, "wb") as f:
            f.write(r.content)
    return path
