import random
# Create An Empty List
numbers=[]

# Generate 8 Random Numbers Between 1 And 100
for i in range(8):
    num = random.randint(1,100)
    numbers.append(num)

# Print The List Of Random Numbers:
print("List Of  Random Integers Between 1 To 100" , numbers)

# Assume First Number is Both The Biggest And The Smallest:
biggest = numbers[0]
smallest = numbers[0]

# Loop Through The List To Find The Biggest And Smallest Numbers:
for n in numbers:
    if n>biggest:
        biggest = n
    if n<smallest:
        smallest = n

# Print The Biggest And Smallest Numbers:
print("Biggest Number Is:", biggest)
print("Smallest Number Is:", smallest)