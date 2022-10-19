#Ayush Sharma

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))


if (a<b and a<c):
    print(a," is Smaller")
elif (b<a and b<c):
    print(b," is Smaller")
else:
    print(c," is Smaller")