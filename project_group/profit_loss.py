import read_file

"""
Converts the data based on exchange_rate. -> data * exchange_rate
"""
def conversion(exchange_rate):
    data = read_file.profit_and_loss()
    data.pop(0)
    for i in range(len(data)):
        data[i][1] = float(data[i][1]) * float(exchange_rate)
        data[i][2] = float(data[i][2]) * float(exchange_rate)
        data[i][3] = float(data[i][3]) * float(exchange_rate)
        data[i][4] = float(data[i][4]) * float(exchange_rate)

    return data

"""
return the difference in net profit between each day. Highlight days the days where net profit is lower than previous
"""
def diff_in_profit(data):
    diff = []
    for i in range(1, len(data)):
        if(data[i][2] < data[i-1][2]):
            diff.append(data[i])

    return diff

"""
Entry Function for Profit and Loss
"""
def profit_lost(exchange_rate):
    data = conversion(exchange_rate)
    diff = diff_in_profit(data)
    return diff