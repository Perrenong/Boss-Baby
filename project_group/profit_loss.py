import csv
profit_and_loss = []
prev_figure = profit_and_loss
with open (r"/Users/kylielxe/Desktop/school/Boss-Baby/project_group/csv_reports/Profit and Loss.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0], line[1], line[2], line[3], line[4])
        profit_and_loss.append(line)
        #print(profit_and_loss)
        for line in reader:
            #print(line)
            for value in line:
                profit_and_loss.append(value)
print(profit_and_loss)

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
