import codecs
import csv


def get_data_from_csv(file):
    csvReader = csv.DictReader(codecs.iterdecode(file.file, 'utf-8'))
    data = []
    for row in csvReader:
        row['zip'] = int(row.get('zip'))
        row['lat'] = float(row.get('lat'))
        row['lng'] = float(row.get('lng'))
        data.append(row)
    file.file.close()
    return data