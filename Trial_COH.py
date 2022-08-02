import csv
Cash_on_hand = []
<<<<<<< HEAD
with open (r"\NP_PFB\Boss-Baby\project_group\csv_reports\Cash on Hand.csv", "r") as file:
=======
with open (r"\Boss_baby_PFB\Boss-Baby-1\project_group\csv_reports\Cash on Hand.csv", "r") as file:
    
>>>>>>> 690e0369c48d551ec4f6b1f0a031b0913a02ecc1
    reader = csv.reader(file)
    for line in reader:
        # print(line[0],line[1])
        Cash_on_hand.append(line)
print(Cash_on_hand)
print()


<<<<<<< HEAD
# flag_list = []
# for value in Cash_on_hand:
#     COH = value
#     prev_figure = ((COH[0][1]))
#     print(prev_figure)
    # if COH >= prev_figure:
    #     print(COH)
    # elif 
    # else:
    #     print("End of day 50")


=======
flag_list = []
prev_figure = (Cash_on_hand[0][1])

flag_list = prev_figure
for x in flag_list: 
    print(x) 

# grade = 60
 
# if grade >= 65:
#     print("Passing grade")
 
# else:
#     print("Failing grade")

# for value in Cash_on_hand:
#     if value >= prev_figure:
#         print(value)

print (prev_figure)
>>>>>>> 690e0369c48d551ec4f6b1f0a031b0913a02ecc1





# figures = flag_list
# if figures >= prev_figure:
#     print(num, "is a positive number.")
# print("This is always printed.")

# num = -1
# if num > 0:
#     print(num, "is a positive number.")
# print("This is also always printed.")


