import csv

Cash_on_hand = []
with open (r"\NP_PFB\Boss-Baby\csv_reports\cash-on-hand-usd.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0],line[1])
        Cash_on_hand.append(line)
print(Cash_on_hand)
print()


flag_list = []
for COH in Cash_on_hand["Cash on Hand"]:
    COH = 


