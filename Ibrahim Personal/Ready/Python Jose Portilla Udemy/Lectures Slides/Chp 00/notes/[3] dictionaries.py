price_lookup = {'apples': 2.99, 'oranges':3.45, 'kiwi':2.89}
price_lookup['oranges']

# KEYS SHOULD ALWAYS BE STRINGS, VALUES CAN BE ANY DATATYPE
# IT can also hold any datatypes

d = {'k1':123, 'k2':[0,1,2], 'k3':{'insideKey':100}}
d['k3']['insideKey']
d['k2'][2]

# we can also use stack calls on a single onject to do a job because of the 
# flexibility python offers

d = {'key1': ['a', 'b', 'c']}
my_capital_c = d['key1'][2].upper()

# you can also add/ modify key/ value pairs

d['key2'] = 'Jebaaaaa'
d['key2'] = "Dangal"

# you can also return all keys values pairs using the methods

d.values()
d.keys()
d.items() # This returns the items in tuples

# if you would like to print dictionaries in order you have
# to use orderedDict