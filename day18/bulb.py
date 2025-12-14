n=int(input("Enter the number of bulbs:"))
bulb=[]
for i in range(n):
    a=int(input("Enter the number of bulbs in machine:"))
    bulb.append(a)
print(min(bulb)*n)