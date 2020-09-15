import csv
import json
import os


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
        csvfields = 'gameId', 'gameDuration', 'level', 'lastRound', 'Ranked', 'ingameDuration', 'combination', 'champion'
        csvReader = csv.DictReader(csvf, fieldnames=csvfields)
        # skip the header because it fucks things over
        next(csvReader, None)

        a = [
            'gameId', 'gameDuration', 'level',
            'lastRound', 'Ranked', 'ingameDuration'
            ]
        b = ['combination', 'champion']

        # for each row we see...
        #       "gameId": str
        #       "gameDuration": str
        #       "level": str
        #       "lastRound": str
        #       "Ranked": str
        #       "ingameDuration": str
        #       "combination": string dict
        #       "champion": string dict
        # take the key which is the row['gameid'] and define as our key
        # for each str field, use dict comprehension to add to a temp dict
        # for each str_dict, use eval to convert str> dict and add to temp
        # add temp dict to full data dict with the key as the key
        for row in csvReader:
            key = row['gameId']
            temp = {field: row[field] for field in a}
            temp['combination'] = eval(row['combination'])
            temp['champion'] = eval(row['champion'])
            data[key] = temp

    # use the json.dumps() with json writer to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

    print('CONVERSION COMPLETE')


main()
