# Data getters
from unittest import result
import api
import read_file

# Data processors
import cash_on_hand
import profit_loss
import overheads

# Output
import write_file

def main():
    # Get data from API
    forex = api.get_exchange_rate()

    # Perform calculations
    pl = profit_loss.profit_lost(forex)
    coh = cash_on_hand.cash_on_hand(forex)
    oh = overheads.overheads(forex)

    # Output to file
    write_file.summarise(
        exchange_rate=forex,
        oh=oh, 
        pl=pl, 
        coh=coh
    )

main()