n=int(int(input("Enter Queue size:")))
cq=[None]*n
front=-1
rear=-1
max=n
def enqueue():
    global rear,front
    if (rear+1)%max==front:
        print("Queue overflow")
    else:
        C = int(input("Enter element:"))
        if front==-1:
            front=0
        rear = (rear+1)%max
        cq[rear]=C
        print("Element ", C, " added into the queue")

def dequeue():
    global rear,front
    if front==-1:
        print("Queue underflow")
    else:
        e=cq[front]
        if front==rear:
            front=-1
            rear=-1
        else:
            front=(front+1)%max
        print("Dequeued element is:",e)
def display():
    global rear,front
    if front==-1:
        print("Queue is empty")
    else:
        i=front
        while True:
            print(cq[i],end=' ')
            if i==rear:
                break
            i=(i+1)%max
        print()
print("\n1.ENQUEUE \n2.DEQUEUE \n3.Display \n4.EXIT")
while True:
    ch = int(input("\nEnter your choice:"))
    if ch == 1:
        enqueue()
    elif ch == 2:
        dequeue()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("Invalid choice")