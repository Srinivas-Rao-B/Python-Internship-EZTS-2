class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def addbegin(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
        else:
            n = self.head
            while n.next != self.head:
                n = n.next
            newnode.next = self.head
            n.next = newnode
            self.head = newnode

    def addend(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            newnode.next = self.head
        else:
            n = self.head
            while n.next != self.head:
                n = n.next
            n.next = newnode
            newnode.next = self.head

    def addpos(self, pos, data):
        newnode = Node(data)
        if pos == 1:
            self.addbegin(data)
            return
        n = self.head
        i = 1
        while i < pos - 1 and n.next != self.head:
            n = n.next
            i += 1
        if i != pos - 1:
            print("Pos out of range")
        else:
            newnode.next = n.next
            n.next = newnode

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
        else:
            n = self.head
            while n.next != self.head:
                n = n.next
            self.head = self.head.next
            n.next = self.head

    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next == self.head:
            self.head = None
            return
        n = self.head
        while n.next.next != self.head:
            n = n.next
        n.next = self.head

    def del_pos(self, pos):
        if self.head is None:
            print("List is empty")
            return
        if pos == 1:
            self.delete_begin()
            return
        n = self.head
        i = 1
        while i < pos - 1 and n.next != self.head:
            n = n.next
            i += 1
        if n.next == self.head or i != pos - 1:
            print("Pos out of range")
        else:
            n.next = n.next.next

    def search(self, data):
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        pos = 1
        while True:
            if n.data == data:
                print(f"Element {data} found at position {pos}")
                return
            n = n.next
            pos += 1
            if n == self.head:
                break
        print(f"Element {data} not found")

    def reverse(self):
        if self.head is None or self.head.next == self.head:
            return
        prev = None
        current = self.head
        start = self.head
        while True:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            if current == start:
                break
        self.head.next = prev
        self.head = prev

    def display(self):
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        while True:
            print(n.data, "-->", end="")
            n = n.next
            if n == self.head:
                break
        print("(head)")

l = CircularLinkedList()
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
