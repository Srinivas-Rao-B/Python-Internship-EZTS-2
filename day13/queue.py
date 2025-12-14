n=int(input("Enter Queue size:"))
q=[None]*n
front=-1
rear=-1
max=n
def enqueue():
    global rear,front
    if rear==max-1:
        print("Queue overflow")
    else:
        C = int(input("Enter element:"))
        rear += 1
        q[rear]=C
        if front==-1:
            front=0
        print("Element ", C, " added into the queue")
def dequeue():
    global rear,front
    if front==-1 or front>rear:
        print("Queue underflow")
    else:
        e=q[front]
        front+=1
        print("Dequeued element is:",e)
def display():
    global rear,front
    if front==-1 or front>rear:
        print("Queue is empty")
    else:
        for i in range(front,rear+1):
            print(q[i],end=' ')
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