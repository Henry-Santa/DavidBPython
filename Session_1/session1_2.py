

total_bill = float(input("Please enter the total bill amount:  ")) # float, ??
party_size = int(input("Please enter the number in your party:  ")) # int, ??
tip_percentage = float(input("Please enter the desired tip percentage (for example,\"20\" for 20%):  ")) # float, ??

tip = total_bill * (tip_percentage / 100) # float, ??
final_bill = total_bill + tip # float, ??
per_person = final_bill / party_size # float, ??

print("A " + str(tip_percentage) + "% tip ($" + str(tip) + ") was added to the bill, for a total of $" + str(final_bill))
print("With " + str(party_size) + " in your party, each person must pay $" + str(per_person))
