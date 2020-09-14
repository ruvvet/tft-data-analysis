import csv
import json
import os
import pandas as pd
from itertools import groupby
from collections import OrderedDict


def main():
    # Ask csv path input
    inputFilePath = str(input('CSV File Path: '))

    csvFilePath = inputFilePath
    print('CSV FILE NAME: ', csvFilePath)
    # D:\PythonProjects\tft-data-analysis\data\TFT_Challenger_MatchData.csv
    filename = os.path.splitext(csvFilePath)[0]
    jsonFilePath = filename + '.json'
    print('JSON FILE NAME:', jsonFilePath)

    # Call the csv_to_json function
    print('CONVERTING...')
    csv_to_json(csvFilePath, jsonFilePath)


# Convert CSV to JSON
def csv_to_json(csvFilePath, jsonFilePath):
    # make empty dict for json data
    data = {}

    # Open dictreader from csv module
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # columns = gameId,gameDuration,level,lastRound,Ranked,ingameDuration,combination,champion
        # Convert each row + add to data dict
        # gameID is primary key

        for rows in csvReader:
            key = rows['gameId']
            data[key] = rows

    # use the json.dumps() with json writer to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

    print('CONVERSION COMPLETE')


# # the messed up version
# def csv_to_json(csvFilePath, jsonFilePath):
#     # make empty dict for json data
#     data = {}

#     # Open dictreader from csv module
#     with open(csvFilePath, encoding='utf-8') as csvf:
#         csvfields = 'gameId', 'gameDuration', 'level', 'lastRound', 'Ranked', 'ingameDuration', 'combination', 'champion'
#         csvReader = csv.DictReader(csvf, fieldnames=csvfields)
#         # IDK what i'm doing here
#         # for row in csvReader:
#         #     key = row['gameId']
#         #     if row['combination']:
#         #         data['combination'] = row
#         #         print('hi', row['combination'])
#         #         for combo in row['combination']:
#         #             print(combo)

#         #     else:
#         #         data[key] = row

#     # use the json.dumps() with json writer to dump data
#     with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
#         jsonf.write(json.dumps(data, indent=4))

#     print('CONVERSION COMPLETE')


main()
