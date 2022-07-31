import csv

full_list_1 = []
with open (r"\NP_PFB\Boss-Baby\csv_reports\cash-on-hand-usd.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0], line[1])
        full_list_1.append(line)
print(full_list_1)
print()



full_list_2 = []
with open (r"\NP_PFB\Boss-Baby\csv_reports\overheads.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0], line[1])
        full_list_2.append(line)
print(full_list_2)
print()



full_list_3 = []
with open (r"\NP_PFB\Boss-Baby\csv_reports\profit-and-loss-usd.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0], line[1], line[2], line[3], line[4])
        full_list_3.append(line)
print(full_list_3)

