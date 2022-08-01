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



list = []
for week, forex in data["Time Series FX (Weekly)"].items():
    closing_price=(float(forex["4. close"]))
    list.append(closing_price)
    
average_forex_price = sum(list)/len(list)
print(f"The mean of the weekly closing forex price is ${round(average_forex_price,2)}")



flag_list = []
for COH in Cash_on_hand["Cash on Hand"]:
    COH = 


