# two.py

	
import one_1

print ("Top level in two.py")

one_1.func()

if __name__ == "__main__":
	print("Two.py is being run directly!")
else:
	print("Two.py has been imported")
	
