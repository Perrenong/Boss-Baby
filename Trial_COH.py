import csv
Cash_on_hand = []
with open (r"\NP_PFB\Boss-Baby\project_group\csv_reports\Cash on Hand.csv", "r") as file:
    reader = csv.reader(file)
    for line in reader:
        # print(line[0],line[1])
        Cash_on_hand.append(line)
print(Cash_on_hand)
print()


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




