grade = 0
if (grade >= 95 and grade <= 100):
    print("A+")
elif (grade >= 85 and grade <= 94):
    print("A")
elif (grade >= 80 and grade <= 84):
    print("B+")
elif (grade >= 70 and grade <= 79):
    print("B")
elif (grade >= 60 and grade <= 69):
    print("C") 
elif (grade >= 50 and grade <= 59):
    print("D")
elif (grade >= 0 and grade <= 49):
    print("F")
else:
    print("Invalid grade")
        
ict = int(input("Enter the marks of ICT: "))
grade = ict
print("ICT: ", grade)
pf = int(input("Enter the marks of PF: "))
cal = int(input("Enter the marks of CALCULAS: "))
eng = int(input("Enter the marks of ENGLISH: "))
phy = int(input("Enter the marks of PHYSICS: "))
isl = int(input("Enter the marks of ISLAMIC STUDIES: "))
