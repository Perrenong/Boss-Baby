import csv
from sqlite3.dbapi2 import _Statement

Cash_on_hand = []
with open (r"\NP_PFB\Boss-Baby\project_group\csv_reports\Cash on Hand.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0],line[1])
        Cash_on_hand.append(line)
print(Cash_on_hand)
print()


flag_list = []
prev_figure = (Cash_on_hand[0][1])
for value in Cash_on_hand:
    if value >= prev_figure:
        print(value)

# continute_Statement



