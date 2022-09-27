#Get three numbers from user in specific veriable
#using three numbers dolve this equation = a + b +ca/b(2a+3b)
#Display result to user

A = int(input("Enter First Number :\n"))
B = int(input("Enter Second Number :\n"))
C = int(input("Enter Third Number :\n"))

Result = (A + B + C) * (A / B) * (2 * A + 3 * B)
print("The Result of this Equation is :\n", Result)
