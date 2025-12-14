print("Enter marital status(u for unmarried, m for married):")
mst=input().lower()
if mst=='u':
    gen=input("Enter gender(m for male f for female):").lower()
    age=int(input("Enter age:"))
    if((gen=='m')and age<=30):
        print("Eligible for insurance")
    if((gen=='f')and age<=25):
        print("Eligible for insurance")
    else:
        print("Not eligible for insurance")
else:
    if mst=='m':
        print("Eligible for insurance")
    else:
        print("Invalid input")
