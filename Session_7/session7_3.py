
# your 'def' function here (PLEASE INCLUDE the below code with your function)
def tipcalc(bill : float | int, number_in_party : int, percent : float | int):      # float, 100.0 and int, 4 and int, 20

    if bill <= 0 or number_in_party <= 0:                                           # bool, False
        raise ValueError("'bill' and 'number in party' must be greater than 0")
    
    return (bill + (bill * percent/100))/number_in_party                            # float, 30.0

total = 100.0                         # DO NOT REFER TO THESE
num = 4                               # VARIABLES INSIDE
tip_pct = 20                          # THE FUNCTION!

share = tipcalc(total, num, tip_pct)  # total bill of 100, 4 in party, 20% tip
print(share)                          # 30.0

share = tipcalc(150, 3, 15)           # total bill of 150, 3 in party, 15% tip
print(share)                          # 57.5