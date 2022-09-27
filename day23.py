#Write python program to get name of week and show "Holiday"
#if user input Sunday

Weekname = input("Enter a week name:\n")

if(Weekname == 'Sunday' or Weekname == 'sunday'):
    print("Its Holiday\n")
else:
    print("Its no Holiday")