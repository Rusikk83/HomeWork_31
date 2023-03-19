import json
import csv

def csv_to_json(csv_filename, json_filename):
    with open(csv_filename,  encoding='utf-8') as csv_file:

        mydata = []

        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            mydata.append(row)

    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(mydata, ensure_ascii=False))

csv_to_json("ads.csv", "ads.json")
csv_to_json("categories.csv", "categories.json")
