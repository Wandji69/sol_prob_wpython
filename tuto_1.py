# Ask the use to input their name and assign it to a variable named name
# name = input("What is your name ")
# Print hello followed by the name.
#print("Hello", name)


# Ask the user to input two number and store them in num1 & num2
num1, num2 = input("Enter two numbers ").split()
# convert the string to regular number
num1 = int(num1)
num2 = int(num2)
# Add the values entered and store them in sum
sum = num1 + num2
# Substract the values entered and store them in difference
difference = num1 - num2
# Multiply the values entered and store them in product
product = num1 * num2
# Divide the values entered and store them in qoutient
qoutient = num1 / num2
# Modules the values entered and store them in remainder
remainder = num1 % num2

print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, qoutient))
print("{} % {} = {}".format(num1, num2, remainder))
