n=int(input("Enter Queue size:"))
que=[None]*n
front=-1
rear=-1
max=n
class node:
    def __init__(self,data):
        self.data=data
        self.ref=None   
class circularqueuelinkedlist:
    def __init__(self):
        self.head=None

    def enqueue(self):
        global rear,front
        if (rear+1)%max==front:
            print("Queue overflow")
        else:
            C = int(input("Enter element:"))
            newnode=node(C)
            if self.head is None:
                self.head=newnode
                newnode.ref=self.head
                front=0
                rear=0
            else:
                n=self.head
                while n.ref!=self.head:
                    n=n.ref
                n.ref=newnode
                newnode.ref=self.head
                rear=(rear+1)%max
            print("Element ", C, " added into the queue")

    def dequeue(self):
        global rear,front
        if front==-1:
            print("Queue underflow")
        else:
            e=self.head.data
            if front==rear:
                self.head=None
                front=-1
                rear=-1
            else:
                n=self.head
                while n.ref!=self.head:
                    n=n.ref
                n.ref=self.head.ref
                self.head=self.head.ref
                front=(front+1)%max
            print("Dequeued element is:",e)

    def display(self):
        global rear,front
        if front==-1:
            print("Queue is empty")
        else:
            n=self.head
            while True:
                print(n.data,end=' ')
                if n.ref==self.head:
                    break
                n=n.ref
            print()
print("\n1.ENQUEUE \n2.DEQUEUE \n3.Display \n4.EXIT")
l=circularqueuelinkedlist()
while True:
    ch = int(input("\nEnter your choice:"))
    if ch == 1:
        l.enqueue()
    elif ch == 2:
        l.dequeue()
    elif ch == 3:
        l.display()
    elif ch == 4:
        break
    else:
        print("Invalid choice")