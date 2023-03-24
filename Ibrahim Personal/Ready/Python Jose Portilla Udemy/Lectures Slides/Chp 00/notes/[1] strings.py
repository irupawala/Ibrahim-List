print ("Hello World"[-3]) # to print r
print ("Hello World"[8]) # to print r
print ('Hello \nworld') # new line
print ('Hello \tworld') # new tab
len("I am") # length of the string

##
my_string = "Hello World"
my_string[-3]

##
my_string = "abcdefg"
my_string[1:]
my_string[:1]
my_string[::1]

# very interseting code please read
my_string = "abcdefg"
my_string[::-1]

# Strings are immutable, You cannot modify individual element of a string
# To modify it you have to use concatenation

my_string = "Sam"
my_string[0] = "P" # This won't work

# To make it Pam use this

my_string_last_letters = my_string[:1]
my_modified_string = "P" + my_string_last_letters

# Multiplacation can be used to concatenate multiple strings at a time

letter = 'z'
letter = 10*letter
print letter

# To use the methods for the string type variable_name. and you will find the list of the methods available
# some of the methods are as follows
# note that the methods won't modify the variable, for that you need reassignment

x = "Hello World"
x.upper()
x.lower()

###
x = "Hi this is a string"
x.split() # creates the list based on the white space or based on the letter you pass in
x.split('i')

# String Interpolation: Nothing but inserting a variable to a string for printing
# There are two methods for this
# 1. .format()
# 2. f-strings (formatted string literals)

print ("This is a string {}".format("INSERTED"))
print ("The {} {} {}".format("fox", "brown", "quick"))
print ("The {2} {1} {0}".format("fox", "brown", "quick"))
print ("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))
print ("The {f} {f} {f}".format(f="fox", b="brown", q="quick"))

# formatting can also be used to control the precision of the result
# Float formatting follows "{value:width.precision f}"
result = 100/777
print (result)
print ("The result is {r:10.3}".format(r = result)) # width is how long you want the result to be
print ("The result is {r:10.5}".format(r = result))

# f-strings literals
name = "Ibrahim"
print(f"Hello, my name is {name}")

name = "Ibrahim"
age = 27

print(f"{name} is {age} years old") 