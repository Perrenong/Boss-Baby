import csv

Cash_on_hand = []
with open (r"\NP_PFB\Boss-Baby\project_group\csv_reports\Cash on Hand.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0],line[1])
        Cash_on_hand.append(line)
print(Cash_on_hand)
print()


Overheads = []
with open (r"\NP_PFB\Boss-Baby\csv_reports\overheads.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0], line[1])
        Overheads.append(line)
print(Overheads)
print()



Profit_and_lose = []
with open (r"\NP_PFB\Boss-Baby\csv_reports\profit-and-loss-usd.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0], line[1], line[2], line[3], line[4])
        Profit_and_lose.append(line)
print(Profit_and_lose)
print()








