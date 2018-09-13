#add function
def add(num1, num2):
	return num1 + num2
#subtract function
def subtract(num1, num2):
	return num1 - num2
#divide function which provides an integer output and a remainder 
def divide(num1, num2):
	return str(int(num1 / num2)) + ' Remainder:' + str(int(num1%num2))
#multiply function 
def multiply(num1, num2):
	return num1 * num2
	

def main():
#diplays options
	print("0 Exit")
	print("1 Add")
	print("2 Subtract")
	print("3 Divide")
	print("4 Multiply")
#ask user for input
	operation = input("Please select from the options above:")
#if statement which controls which option is selected
	if(operation >= chr(49) and operation <= chr(52)):
		val1 = int(input("Enter First Value:"))
		val2 = int(input("Enter Second Value:"))
		if(operation == chr(49)):
			print(add(val1, val2))
		elif(operation == chr(50)):
			print(subtract(val1, val2))
		elif(operation == chr(51)):
			print(divide(val1, val2))
		elif(operation == chr(52)):
			print(multiply(val1, val2))
	elif(operation == chr(48)):
		exit()
	else:
		print("Bad input")
main()