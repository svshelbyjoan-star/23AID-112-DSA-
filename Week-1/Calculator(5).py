# getting both the inputs as String
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
# converting the inputs to integer
num1 = int(num1)
num2 = int(num2)
# performing addition
sum = num1 + num2
# printing the sum
print("The sum is:", sum)
# performing subtraction
difference = num1 - num2
# printing the difference
print("The difference is:", difference)
# performing multiplication
product = num1 * num2
# printing the product
print("The product is:", product)
# Finding the greater number
if num1 > num2:
    print(num1, "is greater than", num2)
elif num2 > num1:
    print(num2, "is greater than", num1)
else:
    print("Both numbers are equal")
    