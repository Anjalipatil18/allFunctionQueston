user_input=raw_input("enter the operation==")
def add_numbers(number_x, number_y,operation):
	if operation == "addition":
		return number_x + number_y
	elif operation == "subtraction":
		subtraction=number_x-number_y
		return subtraction
	elif operation == "multiplication":    	
		return number_x*number_y
	elif operation == "division":
		return number_x/number_y
	else:
		modulus=number_x%number_y
  		return modulus
print add_numbers(4,5,user_input)