import read_file

"""
Converts the data based on exchange_rate. -> data * exchange_rate
"""
def conversion(exchange_rate):
    data = read_file.overheads()
    data.pop(0)
    for i in range(len(data)):
        data[i][1] = float(data[i][1]) * float(exchange_rate)
    return data

"""
Returns the highest overhead in the data.
"""
def highest_overhead(data):
    # Temporary Storage to track the highest value
    highest_num = 0
    highest_index = 0

    # Loop through data and get the highest value and it's index
    for i in range(len(data)):  
        if(float(data[i][1]) > highest_num):
            highest_num = float(data[i][1])
            highest_index = i
    
    # save the highest value and it's index in highest_data
    highest_data = data[highest_index]

    # remove the highest value from the data
    data.pop(highest_index)

    # insert it at index 0 the highest value and it's index
    data.insert(0, highest_data)

    return data

"""
Entry Function for Overheads
"""
def overheads(exchange_rate):
    data = conversion(exchange_rate)
    data = highest_overhead(data)
    return data
    