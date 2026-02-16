num=int(input("Enter your marks: "))
if num>=90:
    print("Grade: A")
elif num>=80:
    print("Grade: B")
elif num>=70:
    print("Grade: C")
elif num>=60:
    print("Grade: D")
else:
    print("Grade: F")
    if num<0 or num>100:
        print("Invalid marks entered. Please enter a number between 0 and 100.")    
    else:
        print("Your grade is F. Better luck next time!")