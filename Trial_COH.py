import csv

Cash_on_hand = []
with open (r"\Boss_baby_PFB\Boss-Baby-1\project_group\csv_reports\Cash on Hand.csv", "r") as file:
    
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        # print(line[0],line[1])
        Cash_on_hand.append(line)
print(Cash_on_hand)
print()


flag_list = []
prev_figure = (Cash_on_hand[0][1])

def difference():
    '''
    '''
    if distance <= 32:
            return distance * 0
        elif 33 <= distance <= 40:
            return (32 * 0) + ((distance - 32) * 325)
        elif 41 <= distance <= 48:
            return (32 * 0) + (8 * 325) + ((distance - 40) * 550)
        else:
            distance > 48
            return (32 * 0) + (8 * 325) + (8 * 550) + ((distance - 48) * 600)
# for value in Cash_on_hand:
#     if value >= prev_figure:
#         print(value)

print (prev_figure)





# figures = flag_list
# if figures >= prev_figure:
#     print(num, "is a positive number.")
# print("This is always printed.")

# num = -1
# if num > 0:
#     print(num, "is a positive number.")
# print("This is also always printed.")


# # figure = prev_figure
# # for x in figure: 
# #     print(x) 