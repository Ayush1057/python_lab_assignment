#Ayush Sharma

num = int(input("Enter The number: "))
exp = int(input("Enter The power: "))

power = 1
for x in range(0,exp):
    power = power * num

print("Result: ",power)
