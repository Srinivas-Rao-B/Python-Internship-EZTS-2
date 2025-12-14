# #hashingchained using linked list
# size=int(input("Enter size of hash table:"))
# hash_table=[None]*size
# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.next = None

# def insert(key):
#     index=key%size
#     new_node=Node(key)
#     if hash_table[index] is None:
#         hash_table[index]=new_node
#     else:
#         current=hash_table[index]
#         while current.next:
#             current=current.next
#         current.next=new_node
#     print("Key inserted at index:",index)

# def display():
#     print("\n Hash Table:")
#     for i in range(size):
#         print(i,"->",end=" ")
#         current=hash_table[i]
#         while current:
#             print(current.key,"->",end=" ")
#             current=current.next
#         print("None")

# def delete(key):
#     index=key%size
#     current=hash_table[index]
#     prev=None
#     while current and current.key!=key:
#         prev=current
#         current=current.next
#     if current is None:
#         print("Key not found")
#         return
#     if prev is None:
#         hash_table[index]=current.next
#     else:
#         prev.next=current.next
#     print("Key deleted:",key)

# def search(key):
#     index=key%size
#     current=hash_table[index]
#     while current:
#         if current.key==key:
#             print("Key found at index:",index)
#             return
#         current=current.next
#     print("Key not found")

# print("\n1.Insert \n2.Delete \n3.Search \n4.Display \n5.Exit")
# while True:
#     choice=int(input("Enter your choice:"))
#     if choice==1:
#         key=int(input("Enter key to be inserted:"))
#         insert(key)
#     elif choice==2:
#         key=int(input("Enter key to be deleted:"))
#         delete(key)
#     elif choice==3:
#         key=int(input("Enter key to be searched:"))
#         search(key)
#     elif choice==4:
#         display()
#     elif choice==5:
#         display()
#         break
#     else:
#         print("Invalid choice")  

# Hashing with chaining using linked list
size = 10
hash_table = [None] * size

class Node:
    def __init__(self, key, original_key):
        self.key = key              # numeric hash value
        self.original_key = original_key  # keep original key for display
        self.next = None

def get_hash(key):
    if isinstance(key, str):
        return sum(ord(c) for c in key)
    elif isinstance(key, int):
        return key
    else:
        raise ValueError("Invalid key type. Only integers and strings are allowed.")

def insert(key):
    hash_val = get_hash(key)
    index = hash_val % size
    new_node = Node(hash_val, key)
    if hash_table[index] is None:
        hash_table[index] = new_node
    else:
        current = hash_table[index]
        while current.next:
            current = current.next
        current.next = new_node
    print("Key inserted at index:", index)

def display():
    print("\nHash Table:")
    for i in range(size):
        print(i, "->", end=" ")
        current = hash_table[i]
        while current:
            print(current.original_key, "->", end=" ")
            current = current.next
        print("None")

def delete(key):
    hash_val = get_hash(key)
    index = hash_val % size
    current = hash_table[index]
    prev = None
    while current and current.key != hash_val:
        prev = current
        current = current.next
    if current is None:
        print("Key not found")
        return
    if prev is None:
        hash_table[index] = current.next
    else:
        prev.next = current.next
    print("Key deleted:", key)

def search(key):
    hash_val = get_hash(key)
    index = hash_val % size
    current = hash_table[index]
    while current:
        if current.key == hash_val:
            print("Key found at index:", index)
            return
        current = current.next
    print("Key not found")

print("\n1.Insert \n2.Delete \n3.Search \n4.Display \n5.Exit")
while True:
    choice = int(input("Enter your choice:"))
    if choice == 1:
        key = input("Enter key to be inserted:")   # can be string or number
        try:
            key = int(key) if key.isdigit() else key
            insert(key)
        except ValueError as e:
            print(e)
    elif choice == 2:
        key = input("Enter key to be deleted:")
        key = int(key) if key.isdigit() else key
        delete(key)
    elif choice == 3:
        key = input("Enter key to be searched:")
        key = int(key) if key.isdigit() else key
        search(key)
    elif choice == 4:
        display()
    elif choice == 5:
        display()
        break
    else:
        print("Invalid choice")
