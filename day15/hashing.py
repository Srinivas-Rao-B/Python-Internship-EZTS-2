# size=int(input("Enter size of hash table:"))
# hashh_t=[-1]*size
# def insert(key):
#     index=key%size
#     org_ind=index
#     while hashh_t[index]!=-1:
#         index=(index+1)%size
#         if index==org_ind:
#             print("Hash table is full")
#             return
#     hashh_t[index]=key
#     print("Key inserted at index:",index)

# def display():
#     print("\n Hash Table:")
#     for i in range(size):
#         print(i,"->",hashh_t[i])

# def delete(key):
#     index=key%size
#     org_ind=index
#     while hashh_t[index]!=key:
#         index=(index+1)%size
#         if hashh_t[index]==-1 or index==org_ind:
#             print("Key not found")
#             return
#     hashh_t[index]=-1
#     print("Key deleted:",key)

# def search(key):
#     index=key%size
#     org_ind=index
#     while hashh_t[index]!=key:
#         index=(index+1)%size
#         if hashh_t[index]==-1 or index==org_ind:
#             print("Key not found")
#             return
#     print("Key found at index:",index)

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

# Hashing using linear array (no linked list)
size = 10
hash_table = [-1] * size

def get_hash(key):
    if isinstance(key, str):
        return sum(ord(c) for c in key) % size
    elif isinstance(key, int):
        return key % size
    else:
        raise ValueError("Only integers or strings allowed")

def insert(key):
    index = get_hash(key)
    # linear probing in case of collision
    original_index = index
    while hash_table[index] is not None:
        index = (index + 1) % size
        if index == original_index:
            print("Hash table overflow")
            return
    hash_table[index] = key
    print(f"Key inserted at index: {index}")

def delete(key):
    index = get_hash(key)
    original_index = index
    while hash_table[index] is not None:
        if hash_table[index] == key:
            hash_table[index] = None
            print(f"Key deleted: {key}")
            return
        index = (index + 1) % size
        if index == original_index:
            break
    print("Key not found")

def search(key):
    index = get_hash(key)
    original_index = index
    while hash_table[index] is not None:
        if hash_table[index] == key:
            print(f"Key found at index: {index}")
            return
        index = (index + 1) % size
        if index == original_index:
            break
    print("Key not found")

def display():
    print("\nHash Table:")
    for i in range(size):
        print(f"{i} -> {hash_table[i]}")

# Menu
print("\n1.Insert \n2.Delete \n3.Search \n4.Display \n5.Exit")
while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        key = input("Enter key to be inserted: ")
        key = int(key) if key.isdigit() else key
        insert(key)
    elif choice == 2:
        key = input("Enter key to be deleted: ")
        key = int(key) if key.isdigit() else key
        delete(key)
    elif choice == 3:
        key = input("Enter key to be searched: ")
        key = int(key) if key.isdigit() else key
        search(key)
    elif choice == 4:
        display()
    elif choice == 5:
        display()
        break
    else:
        print("Invalid choice")
