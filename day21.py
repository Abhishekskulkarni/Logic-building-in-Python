#Write A python Program to Get 5 number from user in Array 
#and sum All number and display

import array as arr
inum = arr.array('i',[])
s = 0

for i in range(5):
    inum.append(int(input("Enter a number to store in the array:\n")))

ino = inum[0]

for j in range(5):
    print(inum[j])
    if(inum[j] > ino):
        ino = inum[j]
print("Max Number = "+str(ino))