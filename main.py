from flask import Flask, jsonify
import csv
import pandas


app = Flask(__name__)

@app.route('/meteoinfo', methods=['GET'])
def getMeteoInfo():
    with open('forecast_dataset (2).csv', 'r') as f:
        data1 = csv.DictReader(f, fieldnames = ['DateTime', 'T', 'U', 'Сl', 'I', 'P', 'FF', 'P0'], delimiter=',')
        json1 = {}
        fieldnames = ['T', 'U', 'Сl', 'I', 'P', 'FF', 'P0']
        for row in data1:
            print(row)
            json2 = {}
            for key in fieldnames:
                json2[key] = row[key]
            json1[row['DateTime']] = json2
    return jsonify(json1)

if __name__=="__main__":
    app.run(host='127.0.0.1', threaded=True, debug=True)