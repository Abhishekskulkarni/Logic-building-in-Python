#write a python program to check Alpha Character Whether 
#Vowel or Consonant

ichar = input("Enter character:\n")

if((ichar == 'a') or (ichar == 'e') or (ichar == 'i')
   or (ichar == 'o') or (ichar == 'u')):
    print( ichar,": is Vowel ")
else:
    print(ichar,": is Consonant")
    