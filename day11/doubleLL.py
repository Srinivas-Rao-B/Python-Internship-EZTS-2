class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def addbegin(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode

    def addend(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = newnode
            newnode.prev = n

    def addpos(self, pos, data):
        newnode = Node(data)
        if pos == 1:
            self.addbegin(data)
            return
        n = self.head
        i = 1
        while n is not None and i < pos - 1:
            n = n.next
            i += 1
        if n is None:
            print("Pos out of range")
        else:
            newnode.next = n.next
            if n.next is not None:
                n.next.prev = newnode
            n.next = newnode
            newnode.prev = n

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def del_pos(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 1:
            self.delete_begin()
            return
        n = self.head
        i = 1
        while n is not None and i < pos:
            n = n.next
            i += 1
        if n is None:
            print("Pos out of range")
        else:
            if n.next is not None:
                n.next.prev = n.prev
            if n.prev is not None:
                n.prev.next = n.next

    def search(self, data):
        n = self.head
        pos = 1
        while n is not None:
            if n.data == data:
                print(f"Element {data} found at position {pos}")
                return
            n = n.next
            pos += 1
        print(f"Element {data} not found")

    def reverse(self):
        if self.head is None:
            return
        n = self.head
        while n is not None:
            n.next, n.prev = n.prev, n.next
            if n.prev is None:
                self.head = n
            n = n.prev

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end="")
                n = n.next
            print("null")

l = DoublyLinkedList()
l.addbegin(10)
l.addbegin(20)
l.addbegin(30)
l.display()
l.addend(40)
l.addend(50)
l.addend(60)
l.display()
l.addpos(1, 25)
l.addpos(2, 35)
l.addpos(90, 30)
l.display()
l.delete_begin()
l.display()
l.delete_end()
l.display()
l.del_pos(2)
l.del_pos(1)
l.display()
l.search(50)
l.search(100)
l.reverse()
l.display()
