n=int(input("Enter Stack size:"))
stk=[None]*n
top=-1
max=n
class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        global top
        if self.head==None:
            print("Stack is empty")
        else:
            n=self.head
            while n!=None:
                print(n.data,"->",end=' ')
                n=n.ref
            print("Null")


    def popstk(self):
        global top
        if self.head is None:
            print("Stack is empty")
            return
        else:
            c=self.head.data
            print("Popped element is:",c)
            top-=1
            self.head=self.head.ref

    def pushstk(self,data):
        global top
        if top == max-1:
            print("Stack overflow")
            return
        newnode=node(data)
        newnode.ref=self.head
        self.head=newnode
        top+=1
        print("Element ", data, " pushed into the stack")   

    
    def peek(self):
        global top
        if self.head==None:
            print("Stack is empty")
        else:
            n=self.head
            while n.ref!=None:
                n=n.ref
            print("Peek element is:",n.data)

    def search(self):
        global top
        if self.head==None:
            print("Stack is empty")
        else:
            item=int(input("Enter element to be searched:"))
            n=self.head
            pos=top
            while n!=None:
                if n.data==item:
                    print("Element found at position:",top-pos+1)
                    break
                n=n.ref
                pos-=1
            else:
                print("Element not found")

l=linkedlist()
print("\n1.POP \n2.PUSH \n3.Display \n4.PEEK ELEMENT \n5.SEARCH \n6.EXIT")
while True:
    ch = int(input("\nEnter your choice:"))
    if ch == 1:
        l.popstk()
        l.display()
    elif ch == 2:
        c=int(input("Enter element:"))
        l.pushstk(c)
        l.display()
    elif ch == 3:
        l.display()
    elif ch == 4:
        l.peek()
    elif ch == 5:
        l.search()
    elif ch == 6:
        break
    else:
        print("Invalid Choice")

#stack using linked list
# class Node:
#     def _init_(self, data):
#         self.data = data
#         self.next = None

# class stack:
#     def _init_(self):
#         self.head=None
#         self.stack=[]
#         self.top=-1
#         self.size=0
#     def push(self,data):
#         new_node=Node(data)
#         if self.head ==None:
#             self.head=new_node
#         else:
#             new_node.next=self.head
#             self.head=new_node
#             print(data,"is pushed")
#         self.size+=1
#     def pop(self):
#         if self.head ==None:
#             return None
#         popped_node=self.head
#         self.head=self.head.next
#         self.size-=1
#         return popped_node.data
#     def peek(self):
#         if self.head is None:
#             return None
#         return self.head.data
#     def is_empty(self):
#         return self.size==0
#     def get_size(self):
#         return self.size
#     def display(self):
#         if self.head is None:
#             print("stack is empty")
#         else:
#             n=self.head
#             while n is not None:
#                 print(f"|{n.data}|")
#                 n=n.next
#             print("")
# 1
# s=stack()
# while True:
#     print("\n1.push\n2.pop\n3.display\n4.peek\n5.size\n6.exit")
#     ch=int(input("enter your choice:"))
#     if ch==1:
#         element=int(input("enter the element to be inserted:"))
#         s.push(element)
#     elif ch==2:
#         popped_element=s.pop()
#         if popped_element is None:
#             print("stack underflow")
#         else:
#             print(popped_element,"is popped")
#     elif ch==3:
#         s.display()
#     elif ch==4:
#         top_element=s.peek()
#         if top_element is None:
#             print("stack is empty")
#         else:
#             print("top element is:",top_element)
#     elif ch==5:
#         print("size of stack is:",s.get_size())
#     elif ch==6:
#         break
#     else:
#         print("invalid choice")