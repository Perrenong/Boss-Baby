import csv
<<<<<<< HEAD
profit_and_loss = []
prev_figure = profit_and_loss
with open (r"/Users/kylielxe/Desktop/school/Boss-Baby/project_group/csv_reports/Profit and Loss.csv", "r") as file:
=======

Profit_and_lose = []
with open (r"\Boss_baby_PFB\Boss-Baby-1\project_group\csv_reports\Profit and Loss.csv", "r") as file:
>>>>>>> 0abc2962c877b1bd7d4078c1f7421755eb79b897
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0], line[1], line[2], line[3], line[4])
<<<<<<< HEAD
        profit_and_loss.append(line)
        #print(profit_and_loss)
        for line in reader:
            #print(line)
            for value in line:
                profit_and_loss.append(value)
print(profit_and_loss)
=======
        Profit_and_lose.append(line)

    
print(Profit_and_lose)
print()
>>>>>>> 0abc2962c877b1bd7d4078c1f7421755eb79b897

#profit_and_loss.insert(1, prev_figure)


def profit_and_loss(days, deficit):
    '''
    - The function should return the day 
    - when there will be a deficit amount of the net profit
    '''
    if days >= 40 <= 50 and net_profit > 0:
        return("Yes")
    else:
        return("No")
