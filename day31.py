#write a python program to get 5 colors name from the user 
#in list display that list remove last color and then display 
#that list remove last color and then display all 
#the colors to user

list = []
for i in range(5):
    list.append(input("Enter a color name"))
print("List of the colors are "+str(list))
list.pop()
print("List of the colors are "+str(list))
    

        
    


