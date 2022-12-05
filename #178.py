#Ayush Sharma

def linear(data,n,item):
    for x in data:
        if x == item:
            print("Element found")
            return
    print("not found")

data = [11,22,33,44,55,66,77,88]

linear(data,len(data),21)
