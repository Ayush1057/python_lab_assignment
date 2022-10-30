#Ayush Sharma

num = int(input("Enter the number: "))
exp = int(input("Enter the power: "))

power = 1
i = 1
while (i <= exp):
    power = power * num
    i = i + 1

print("result: ", power)
