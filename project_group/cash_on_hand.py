import csv

Cash_on_hand = []
with open (r"\Boss_baby_PFB\Boss-Baby-1\project_group\csv_reports\Cash on Hand.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0],line[1])
        Cash_on_hand.append(line)
    with open("Cash on Hand.csv",'r') as file:
    #reader = csv.reader(file)
    #header = next(reader)
    #for line in reader:
        #Cash_on_hand.append(line)
        i=0
    for a in Cash_on_hand:
        i += 1
        print(a)
print(Cash_on_hand)
print()