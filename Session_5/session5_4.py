states_file = open('states.csv')    # 'File' Object

lookup_dict = {}                    # Dict, {}

for line in states_file:            # str, 'AL,4908621,52420,Alabama\n'
    line = line.rstrip()            # str, 'AL,4908621,52420,Alabama'
    data = line.split(",")          # List, ['AL', '4908621', '52420', 'Alabama']
    lookup_dict[data[-1]] = data[0] # Dict, {'Alabama' : 'AL'}

print(f"there are {len(lookup_dict)} pairs in the lookup dict")
state_name = input("please enter a state name:  ")                       # str, 'New York'

try:
    print(f"Abbreviation for {state_name} is {lookup_dict[state_name]}") 
except KeyError:
    print(f'no state found with name "{state_name}"')