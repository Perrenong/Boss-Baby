import csv

Profit_and_lose = []
with open (r"\Boss_baby_PFB\Boss-Baby-1\project_group\csv_reports\Profit and Loss.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0], line[1], line[2], line[3], line[4])
        Profit_and_lose.append(line)
print(Profit_and_lose)
print()

