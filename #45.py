#Ayush Sharma

print("Enter 5 numbers: ")
num = []
n = 5
add = 0

for x in range(1,n+1):
    ele = int(input())
    num.append(ele)

for x in num:
    add = add + x

avg = add/n

print(avg)