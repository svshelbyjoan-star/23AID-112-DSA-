grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]
CA =0
CB =0
CC =0
CD =0
for i in grades:
    if i >=90:
        CA +=1
    elif i >=80 and i < 90:
        CB +=1
    elif i >=70 and i < 80:
        CC +=1
    else:
        CD +=1
print("Number of A grades:", CA)
print("Number of B grades:", CB)
print("Number of C grades:", CC)
print("Number of Students who got below 70:", CD)