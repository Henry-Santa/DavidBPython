sample_text = """And since you know you cannot see yourself,
so well as by reflection, I, your glass,
will modestly discover to yourself,
that of yourself which you yet know not of."""

# [YOUR CODE GOES HERE]

find = input("please enter search text:  ")     # str, 'your'
replace = input("please enter replace text:  ") # str, 'yo yo'

final_text = sample_text.replace(find, replace) # str, 'And since you know you cannot see yo yoself, \nso well as by reflection, I, yo yo glass, \n will modestly discover to yo yoself,\n that of yo yoself which you yet know not of.'
occurences = sample_text.count(find)            # int, 4

print("\n" + final_text + "\n")
print(f"{occurences} replacements made.")