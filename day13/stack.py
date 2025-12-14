
n=int(input("Enter stack size:"))
stk=[None]*n
top=-1
max=n
for i in range(n):
    print("Enter element ",i+1,":")
    stk[i]=int(input())
    top+=1
print("Stack is:",stk)

def popstk():
    global top
    if top==-1:
        print("Stack undeflow")
    else:
        e=stk[top]
        top-=1
        print("Popped element is:",e)
def pushstk():
    global top
    if top+1 == max:
        print("Stack overflow")
    else:
        C = int(input("Enter element:"))
        top += 1
        stk[top]=C
        print("Element ", C, " pushed into the stack")
def display():
    global top
    if top==-1:
        print("Stack empty")
    else:
        for i in range(top,-1,-1):
            print(stk[i]) 
        
def peek():
    global top
    if top==-1:
        print("Stack empty")
    else:
        print("Peek element is:",stk[top])
def search():
    global top
    if top==-1:
        print("Stack empty")
    else:
        item=int(input("Enter element to be searched:"))
        for i in range(top,-1,-1):
            if stk[i]==item:
                print("Element found at position:",top-i+1)
                break
        else:
            print("Element not found")

print("\n1.POP \n2.PUSH \n3.Display \n4.PEEK ELEMENT \n5.SEARCH \n6.EXIT")
while True:
    ch = int(input("\nEnter your choice:"))
    if ch == 1:
        popstk()
    elif ch == 2:
        pushstk()
    elif ch == 3:
        display()
    elif ch == 4:
        peek()
    elif ch == 5:
        search()
    elif ch == 6:
        break
    else:
        print("Invalid Choice")