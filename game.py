# This is a valid comment. Make sure to use the '#' key

# Create a main menu with three options:
# 1. Print the product of 3 x 4
# 2. Take in user name, and add 'is gay' at the end
# 3. Quit

def mainMenu(): #Need colon at end
	print "******************"
	print "** A&V Programs **"
	print '**              **' #Notice the single quotes? They still work
	print "** 1. Print 3x4 **"
	print "** 2. User Name **"
	print "** 3. Quit      **"
	print "******************"

def calculation():
	print 3 * 4

def isGay(name):
	print name + " is gay!" #Concatenation right here


isRunning = 1

while (isRunning == 1):
	mainMenu()
	userInput = input("Enter a number: ") #Need to user input() **NOT RAW_INPUT** for anything other than string
	if (userInput > 3 and userInput < 1):
		print "Incorrect response. Try again."
	elif (userInput == 1):
		calculation()
	elif (userInput == 2):
		print "Enter your name: "
		userName = raw_input() #Input as a string
		isGay(userName)
	elif (userInput == 3):
		print "Goodbye!"
		isRunning = 0



