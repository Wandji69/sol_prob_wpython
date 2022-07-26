# Have the user enter thier investment amount and expected interest
# Eache year their investment will incress by their investment + investment *
# interest rate.
# Print out the earning after 10 years

# Ask for the money invested + interest rate
money = input("How much to invest: ")
interest_rate = input("Ecpected interest rate: ")
# convert the value to float
money = float(money)
# convert the value to float and round the percentage rate by 2%
interest_rate = float(interest_rate)*.01
# Cycle through 10 years using a for loop and range from 0 to 9
for i in range(10):
    money = money + (money * interest_rate)
print("Print investment after ten years: {:.2f}".format(money))
# Outpu result.
