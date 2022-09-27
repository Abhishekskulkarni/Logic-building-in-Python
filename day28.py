#write a python program to get marks of student to find its 
#grade 

iMarks = int(input("Enter Makrs of students:\n"))
if(iMarks >= 95):
    print("Student got A+ Grade")
elif(iMarks >= 80):
    print("Student got A Grade")
elif(iMarks >= 70):
    print("Student got B Grade")
elif(iMarks >= 60):
    print("Student got C Grade")
elif(iMarks <= 60):
    print("Student is FAIL")
        

    
    