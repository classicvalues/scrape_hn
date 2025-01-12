
from __future__ import print_function

import csv
import json

import requests
import pandas as pd

fields = ["type", "id", "title", "score", "time", "url", "by", "text"]
url_format = 'https://hacker-news.firebaseio.com/v0/item/%s.json'
max_id = 14269017

fname = "output_1_2.csv"

with open(fname, 'w') as file:
    csvFile = csv.writer(file)
    csvFile.writerow(fields)

    current_id = max_id
    num_responses, num_articles = 0, 0
    while True:
        try:
            url = url_format % current_id
            response = requests.get(url)
            content = response.json()
            content = [str(content.get(k, '')) for k in fields]
            csvFile.writerow(content)

            if num_responses % 10 == 0:
                print("num_responses:", num_responses, "Current ID:", current_id,
                      "num_articles:", num_articles)
            
            current_id = current_id - 3
            num_responses += 1
            if content[0] == "story":
                num_articles += 1
        except Exception as e:
            current_id = current_id - 3
            print(e)
