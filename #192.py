# Ayush Sharma

strng = "hello,world,im,pyhon"

rmv = []

new_str = [" "]

for x in strng:
    if x == ",":
        rmv.append(x)
    else:
        new_str.append(x)

print(new_str)