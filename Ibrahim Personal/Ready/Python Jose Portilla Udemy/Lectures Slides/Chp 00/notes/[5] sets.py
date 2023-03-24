# sets is UNORDERED collections of unique elements
# meaning there cannot be more then one 'a' strings
# In a nutshell there can be only one representative of the same object


my_set = set()
my_set.add(1) # This will return the values in dictionaries but it not a dictionay beacuse it doesn't have any key value pairs
my_set.add(2)
my_set.add(2)

# we can cast a list to a set to get unique values

my_list = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]
set(my_list) # keep in mind sets are unordered collections of uniquw elements
