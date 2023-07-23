#Grade
marks = int(input("Enter your marks: "))
if marks>=90 and marks<=100:
    print("Grade: A")
elif marks>=75 and marks<90:
    print("Grad: B")
elif marks>=50 and marks<75:
    print("Grade: C")
elif marks>=33 and marks<50:
    print("Grade: D")
elif marks>=0 and marks<33:
    print("Grade: F")
else:
    print("Marks are not in range")
