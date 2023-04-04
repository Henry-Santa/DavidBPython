unit_size_1 = float(input("please enter the unit size of Product 1: ")) # float, ??
price_1 = float(input("please enter the price of Product 1: ")) # float, ??
unit_size_2 = float(input("please enter the unit size of Product 2: ")) # float, ??
price_2 = float(input("please enter the price of Product 2: ")) # float, ??

unit_price_1 = price_1 / unit_size_1 # float, ??
unit_price_2 = price_2 / unit_size_2 # float, ??

print("Product 1 costs $0.1 per unit")
print("Product 2 costs $0.15 per unit")

price_compare = round(unit_price_1/unit_price_2, 4) * 100 # float, ??

print("Product 1 is " + str(price_compare) + "% the per-unit cost of Product 2")