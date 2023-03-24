#one.py

def func():
	print ("FUNC() in One.py")

print("Top level in One.py")

if __name__ == '__main__':
	print("One.py is being run directly!")
else:
	print("One.py has been imported!")