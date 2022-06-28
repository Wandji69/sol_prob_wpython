#  Recieve age and store in age
age = eval(input("Enter age: "))

# if age is both greater than and equal to one and less than or equal to 18 IMPORTANT
if age < 5:
    print("To Young for School")
elif age == 5:
    print("Go to Kindergarten")
elif (age > 5) and (age <= 17):
    grade = age - 5
    print("Go to {} grade".format(grade))
else:
    print("Go to College")
