from flask import Flask, jsonify
import csv
import pandas


app = Flask(__name__)

@app.route('/meteoinfo', methods=['GET'])
def getMeteoInfo():
    with open('forecast_dataset (2).csv', 'r') as f:
        data1 = csv.DictReader(f, fieldnames=['DateTime', 'T', 'U', 'Сl', 'I', 'P', 'FF', 'P0'], delimiter=',')
        sum_value = ''
        for row in data1:
            value = '''{\n  "DateTime": "%s",\n  "measurements": {\n  "T": "%s",\n  "U": "%s",\n  "Cl": "%s",\n  "I": "%s",\n  "P": "%s",\n  "FF": "%s",\n  "P0": "%s"\n  }\n}''' % (
            row['DateTime'], row['T'], row['U'], row['Сl'], row['I'], row['P'], row['FF'], row['P0'])
            sum_value = sum_value + value + ',\n'
        sum_value = sum_value[:-2]
    return jsonify({'data':sum_value})


if __name__=="__main__":
    app.run(host='127.0.0.1', threaded=True, debug=True)