from os import rename, listdir
import csv
import json

csvfile = open('tax.csv', 'r')
jsonfile = open('tax.json', 'w')

reader  = csv.reader(csvfile);
for row in reader:
    minimum = row[0]
    maximum = row[1]
    single = {
        "0": row[2],
        "1": row[3],
        "2": row[4],
        "3": row[5]
    }
    hoh = {
        "0": row[2],
        "1": row[3],
        "2": row[4],
        "3": row[5]
    }
    joint = {
        "0": row[6],
        "1": row[7],
        "2": row[8],
        "3": row[9]
    }

    print(minimum)
    print(maximum)
    print(single)
    print(hoh)
    print(joint)

    breakpoints = {
        "min": minimum,
        "max": maximum,
        "single": single,
        "hoh": hoh,
        "joint": joint
    }

    json.dump(breakpoints, jsonfile)
    jsonfile.write(',\n')
