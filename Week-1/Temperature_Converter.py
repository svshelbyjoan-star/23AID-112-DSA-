temp = int(input("Enter the temperature in celsius:"))
farenheit = (temp*(9/5))+32
print("The temperature in farenheit is:", farenheit)
if farenheit < 0 :
    print("Very cold! wear thick jacket")
elif farenheit>0 and farenheit <=15:
    print("Cold , wear a jacket")
elif farenheit>15 and farenheit <=25:
    print("Nice weather")
else:
    print("Hot! Stay hydrated")
