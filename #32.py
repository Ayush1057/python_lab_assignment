#Ayush Sharma

string = "python"

result=''
for i in string:  
    if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        i = ''  
    result += i 
    
print("String after removing the vowels :",result)