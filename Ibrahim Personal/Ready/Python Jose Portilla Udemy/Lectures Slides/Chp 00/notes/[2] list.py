# Can use indexing and slicing just like string

list_1 = [1,2,3]
list_2 = [4,5,6]
list_1 + list_2


# lists are mutable

list_1[0] = "one"

# to concatenate you can use append method

list_1.append(7)

# to remove item we can use pop

list_1.pop() # this will return the popped item also
popped_item = list_1.pop() this will pop off the last item
popped_new = list_1.pop(0)

# reverse indexing also works with lists

popped_new = list_1.pop(-1)

# sort method. SORT METHOD DOES NOT RETURN THE SORTED LIST
new_list = ['a', 'u', 'k', 'f', 'r']
num_list = [4, 7, 1, 0]
new_list.sort() # 
num_list.sort()

sorted_list = num_list.sort() # sorting will occur in place hence
# sorted_list won't be assigned anything and will return none
# if you check the type of sorted_list here then it will be NoneType
# NoneType is type for the None Object, In a nutshell it is a return type for 
# object that doesn't return anything
# but we can do something like this

sorted_list = new_list
print(sorted_list)

# reverse method
num_list.reverse() # this is also inplace meaning it doesn't return
#anything

# How do I index a nested list? For example if I want to grab 2 from [1,1,[1,2]]?
# You would just add another set of brackets for indexing the nested list, for example: my_list[2][1]

