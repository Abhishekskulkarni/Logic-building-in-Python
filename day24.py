#Take two input from User and Perform Arithmatic Operations
iNo1 = int(input("Enter First Number")) 
iNo2 = int(input("Enter Second Number")) 
operator =  input( )

if(operator == '+'):
    iAns = iNo1 + iNo2
    print("Addition is :", iAns)
elif(operator == '-'):
    iAns = iNo1 - iNo2
    print("Substraction is :", iAns)
elif(operator == '/'):
    iAns = iNo1 / iNo2
    print("Division is :", iAns)
elif(operator == '*'):
    iAns = iNo1 * iNo2
    print("Multiplication is :", iAns)
