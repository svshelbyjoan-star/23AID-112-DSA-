L = [12,45,3,98,7,34,21]
C = 0
for i in L:
    print(i)
for i in L:
    if i > 30:
        C+=1
        print(i)
print("Count of numbers greater than 30 is:", C)
