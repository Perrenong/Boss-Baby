# Summarise data from Cash On And, Profit and Loss, and Overheads to text file 
 
""" 
Format the data to be written to file for profit and loss 
""" 
def report_pnl(data): 
    report = "" 
    if(data == []): 
        return "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY" 
         
    for i in data: 
        report += f"[PROFIT DEFICIT] Day: {i[0]}, AMOUNT: {i[2]} \n" 
    return report 
 
""" 
Format the data to be written to file for cash on hand 
""" 
def report_coh(data): 
    report = "" 
    if(data == []): 
        return "[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY" 
     
    for i in data: 
        report += f"[CASH DEFICIT] Day: {i[0]}, AMOUNT: {i[1]} \n" 
     
    return report 
 
""" 
Format the data to be written to file for overheads 
""" 
def report_oh(data): 
    report = f"[HIGHEST OVERHEADS] {data[0][0]}:  {data[0][1]} \n" 
    return report 
 
def summarise(exchange_rate, oh, pl, coh): 
    with open('summary_report.txt', 'w') as report: 
        report.write(f"[REAL TIME CURRENCY EXCHANGE RATE] USD1 = {str(exchange_rate)} \n") 
        report.write('--------------------------------------------------------------- \n') 
        report.write(report_oh(oh)) 
        report.write('--------------------------------------------------------------- \n') 
        report.write(report_pnl(pl)) 
        report.write('--------------------------------------------------------------- \n') 
        report.write(report_coh(coh))