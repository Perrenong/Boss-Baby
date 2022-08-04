import read_file

"""
Converts the data based on exchange_rate. -> data * exchange_rate
"""
def coh_conversion(exchange_rate):
    # Get Data
    data = read_file.cash_on_hand()

    # Remove the header
    data.pop(0)

    # Multiply values of cash on hands by the exchange rate
    for i in range(len(data)):
        data[i][1] = float(data[i][1]) * float(exchange_rate)
    return data

"""
Find the days where Cash-on-Hand is lower than the previous day
"""
def diff_in_coh(data):

    l_days = [] # List of days where the previous day was higher than the current day

    # if the previous day was higher than the current day
    # then append the current day to l_days
    for i in range(len(data)):
        if data[i][1] < data[i-1][1]:
            l_days.append(data[i])
            
    return l_days

"""
Entry Function for Cash-on-Hand
"""
def cash_on_hand(exchange_rate):
    # Applies the two functions above to output the correct data

    data = coh_conversion(exchange_rate) # Converts to SGD
    coh = diff_in_coh(data) # Finds the days where the previous day was higher than the current day
    return coh