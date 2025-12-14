import time
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

    def play_song(self):
        if self.head==None:
            print("play-list is empty")
        else:
            n=self.head
            while True:
                print("now playing",n.data)
                time.sleep(5)
                n=n.next
                if n==self.head:
                    break

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
        print(n.data)

c = CircularLinkedList()
while True:
    print("\n\n #####  MUSIC MENU #####\n 1.Create song \n 2.Playlist \n 3.Select the song \n 4.Play song \n 5.Exit")
    ch =int(input("Enter your choice :"))
    if ch==1:
        n=int(input("How many songs :"))
        for i in range(n):
            song=input("Enter song name :")
            c.addend(song)
    elif ch==2:
        print("Your playlist is :")
        c.display()
    elif ch==3:
        song=input("Search song:")
        c.search(song)
    elif ch==4:
        c.play_song()
    elif ch==5:
        break
    else:
        print("Invalid choice")