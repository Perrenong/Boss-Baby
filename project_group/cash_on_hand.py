import csv

Cash_on_hand = []
with open (r"\Boss_baby_PFB\Boss-Baby-1\project_group\csv_reports\Cash on Hand.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0],line[1])
        Cash_on_hand.append(line)
<<<<<<< HEAD

flag_list = []
if day
num = Cash_on_hand.append(line)
prev_figure = flag_list
flag_list.insert(1, prev_figure) 
print(flag_list)

=======
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
>>>>>>> 676a4f3fe11c7812f63bf9dc84cfeaf43f7e0695
