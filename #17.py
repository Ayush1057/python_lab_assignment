#Ayush Sharma

char = input("Enter the Character: ")
lower = int((char==('a') or char==('e') or char==('i') or char==('o') or char==('u')))
upper = int((char==('A') or char==('E') or char==('I') or char==('O') or char==('U')))

if (lower or upper):
    print("Vowel")
else:
    print("Consonant")