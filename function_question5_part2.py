input1=input("enter the number=")
input2=input("enter the number=")
user_input=raw_input("enter the operation==")
def add_numbers(number_x, number_y,operation):
	if operation == "addition":
		addition = number_x + number_y
		return addition
	elif operation == "subtraction":
		subtraction=number_x-number_y
		return subtraction
	elif operation == "multiplication":    	
		multiplication = number_x*number_y
		return multiplication
	elif operation == "division":
		division=number_x/number_y
		return division
	else:
		modulus=number_x%number_y
  		return modulus
print add_numbers(input1,input2,user_input)
