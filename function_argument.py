numbers_list = [1, 2, 3, 4, 5, 6, 7, 10, -2]
print max(numbers_list)
print"*********************************************************************"
i=0
max=numbers_list[i]
second_max=numbers_list[i]
while i<len(numbers_list):
	if numbers_list[i]>max:
		max=numbers_list[i]
	i=i+1
print max
print"*********************************************"
def say_hello(name):
    print "Hello ", name
    print "Aap kaise ho?"
say_hello("Aatif")
print"*********************************************"

def add_numbers(number1, number2):
    print "Main do numbers ko add karunga."
    print number1 + number2
add_numbers(120, 50)
num_x = 134
num_y = 22
add_numbers(num_x, num_y)

print"***************************************************"

def say_hello_language(name, language):
    if language == "hindi":
        print "Namaste ", name
        print "Aap kaise ho?"
    elif language == "punjabi":
        print "Sat sri akaal ", name
        print "Tuhada ki haal hai?"
    else:
        print "Hello ", name
        print "How are you?"
say_hello_language("Rishabh", "punjabi")
say_hello_language("Armaan", "english")
say_hello_language("Abhishek", "french")
say_hello_language("Kavay", "hindi")
print "*******************************************************************"
def say_hello_people(name_x, name_y, name_z, name_a):
    print "Namaste ", name_x # hindi mein
    print "Alah hafiz ", name_y # urdu mein
    print "Bonjour ", name_z # french mein
    print "Hello ", name_a # english mein
say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev")



