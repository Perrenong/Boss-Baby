from pathlib import Path
import csv

Overheads = []
with open (r"\NP_PFB\Boss-Baby\csv_reports\overheads.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0], line[1])
        Overheads.append(line)
print(Overheads)
print()