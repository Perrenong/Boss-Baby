import csv

def cash_on_hand():
    data = []
    with open('csv_reports\Cash on Hand.csv', 'r',  encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
    return data

def overheads():
    data = []
    with open('csv_reports\overheads.csv', 'r',  encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
    return data

def profit_and_loss():
    data = []
    with open('csv_reports\Profit and Loss.csv', 'r',  encoding='UTF-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
    return data