min=0
max=7000
cap=int(input("Enter the weight of clothes(<7000 gms):"))
if cap==min:
    print("est time: 0 min")
elif cap<=2000:
    print("est time: 25 min")
elif cap<=4000:
    print("est time: 35 min")   
elif cap<=max:
    print("est time: 45 min")
else:
    print("Overload!!")