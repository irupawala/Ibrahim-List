#one.py

def func():
	print ("FUNC() in One.py")

def func1():
	pass

def func2():
	pass

print("Top level in One.py")

if __name__ == '__main__':
	# Run this function if the script is being run directly
	func()
	func1()
	func2()