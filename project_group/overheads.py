import csv

Overheads = []
with open (r"\Boss_baby_PFB\Boss-Baby-1\project_group\csv_reports\overheads.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0], line[1])
        Overheads.append(line)
print(Overheads)
print()