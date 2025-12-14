n=10
k=5
jar=n
order=int(input("Enter your order:"))
if order<=0 or order>=n:
    print("Invalid order")
else:
    jar-=order
    print("No of candies sold:",order)
    print("No of candies left:",jar)
    if(jar<=k):
        jar=n
        print("Jar is refilled")
        print("No of candies left:",jar)