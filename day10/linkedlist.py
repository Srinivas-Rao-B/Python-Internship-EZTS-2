class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def addbegin(self,data):
        newnode=node(data)
        newnode.ref=self.head
        self.head=newnode
    
    def addend(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
        else:
            n=self.head
            while n.ref!=None:
                n=n.ref
            n.ref=newnode

    def addpos(self,pos,data):
        newnode=node(data)
        if pos==1:
            newnode.ref=self.head
            self.head=newnode
            return
        n=self.head
        i=1
        while n!=None and i<pos-1:
            n=n.ref
            i+=1
        if n is None:
            print("Pos out of range")
        else:
            newnode.ref=n.ref
            n.ref=newnode
    def delete_begin(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            self.head=self.head.ref
    def delete_end(self):
        if self.head is None:
            print("list is empty")
            return
        if self.head.ref is None:
            self.head=None
            return
        n=self.head
        while n.ref.ref is not None:
            n=n.ref
        n.ref=None

    def del_pos(self,pos):
        if self.head==None:
            print("list is empty")
            return
        if pos==1:
            self.head=self.head.ref
            return
        n=self.head
        i=1
        while n!=None and i<pos-1:
            n=n.ref
            i+=1
        if n is None or n.ref is None:
            print("pos out of range")
        else:
            n.ref=n.ref.ref

    def display(self):
        if self.head==None:
            print("List is empty")
        else:
            n=self.head
            while n!=None:
                print(n.data,"-->",end="")
                n=n.ref
            print("null")
l=linkedlist()
l.addbegin(10)
l.addbegin(20)
l.addbegin(30)
l.display()
l.addend(40)
l.addend(50)
l.addend(60)
l.display()
l.addpos(1,25)
l.addpos(2,35)
l.addpos(90,30)
l.display()
l.delete_begin()
l.display()
l.delete_end()
l.display()
l.del_pos(2)
l.del_pos(1)
l.display()

#single linked list implementation in python
# class Node:
#     def _init_(self, data):
#         self.data = data
#         self.ref = None
# class LinkedList:
#     def _init_(self):
#         self.head=None
#     def add_begin(self,data):
#         newnode=Node(data)
#         newnode.ref=self.head
#         self.head=newnode
#     def add_end(self,data):
#         newnode=Node(data)
#         if self.head==None:
#             self.head=newnode
#         else:
#             n=self.head
#             while n.ref!=None:
#                 n=n.ref
#             n.ref=newnode
#     def addpos(self,pos,data):
#         newnode=Node(data)
#         n=self.head
#         if pos==1:
#             newnode.ref=self.head
#             self.head=newnode
#             return
#         i=1
#         while n!=None and i<pos-1:
#             n=n.ref
#             i+=1
#         if n is None:
#             print("Pos out of range")
#         else:
#             newnode.ref=n.ref
#             n.ref=newnode
#     def display(self):
#         if self.head==None:
#             print("linked list is empty")
#             return
#         else:
#             n=self.head
#             while n!=None:
#                 print(n.data,"-->",end=" ")
#                 n=n.ref
#             print("NULL")
#     def delete_begin(self):
#         if self.head is None:
#             print("list is empty")
#             return
#         else:
#             self.head=self.head.ref
#     def delete_end(self):
#         if self.head is None:
#             print("list is empty")
#             return
#         if self.head.ref is None:
#             self.head=None
#             return
#         n=self.head
#         while n.ref.ref is not None:
#             n=n.ref
#         n.ref=None
#     def del_pos(self,pos):
#         if self.head==None:
#             print("list is empty")
#             return
#         if pos==1:
#             self.head=self.head.ref
#             return
#         n=self.head
#         i=1
#         while n!=None and i<pos-1:
#             n=n.ref
#             i+=1
#         if n is None or n.ref is None:
#             print("pos out of range")
#         else:
#             n.ref=n.ref.ref
# if _name=="main_":
#     ll=LinkedList()
#     while True:
#         print("1. Add at beginning")
#         print("2. Add at end")
#         print("3. Display")
#         print("4. Add at position")
#         print("5. Delete at beginning")
#         print("6. Delete at end")
#         print("7. Delete at position")
#         print("8. Exit")
#         choice=int(input("enter your choice:"))
#         if choice<=1 or choice>=8:
#             print("invalid choice")
#         if choice==1:
#             data=int(input("enter data:"))
#             ll.add_begin(data)
#         if choice==2:
#             data=int(input("enter data:"))
#             ll.add_end(data)
#         if choice==3:
#             ll.display()
#         if choice==4:
#             pos=int(input("enter the position:"))
#             data=int(input("enter data:"))
#             ll.addpos(pos,data)
#         if choice==5:
#             ll.delete_begin()
#         if choice==6:   
#             ll.delete_end()
#         if choice==7:
#             pos=int(input("enter the position:"))
#             ll.del_pos(pos)
#         if choice==8:
#             break