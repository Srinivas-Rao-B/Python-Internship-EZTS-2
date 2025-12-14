def insert(tree, root, node):
    if node < root:
        if tree[root][0] is None:
            tree[root][0] = node
            tree[node] = [None, None]
        else:
            insert(tree, tree[root][0], node)
    else:
        if tree[root][1] is None:
            tree[root][1] = node
            tree[node] = [None, None]
        else:
            insert(tree, tree[root][1], node)

n = int(input("Enter the number of nodes: "))
root = input("Enter the root node: ")
tree = {root: [None, None]}
for i in range(n - 1):
    node = input("Enter the node: ")
    insert(tree, root, node)
print("\nBinary Tree (Left, Right children):")
for k, v in tree.items():
    print(k, ":", v)

def inorder(tree, root):
    if root:
        if root in tree:
            inorder(tree, tree[root][0])
            print(root, end=" ")
            inorder(tree, tree[root][1])
        else:
            print(root, end=" ")

def preorder(tree, root):
    if root:
        print(root, end=" ")
        if root in tree:
            preorder(tree, tree[root][0])
            preorder(tree, tree[root][1])

def postorder(tree, root):
    if root:
        if root in tree:
            postorder(tree, tree[root][0])
            postorder(tree, tree[root][1])
            print(root, end=" ")
        else:
            print(root, end=" ")

print("\n\nInorder Traversal:")
inorder(tree, root)
print("\nPreorder Traversal:")
preorder(tree, root)
print("\nPostorder Traversal:")
postorder(tree, root)

def height(tree, root):
    if not root or root not in tree:
        return 0
    left = height(tree, tree[root][0])
    right = height(tree, tree[root][1])
    return 1 + max(left, right)

print("\nHeight of the tree:", height(tree, root))

def count_nodes(tree, root):
    if not root:
        return 0
    if root not in tree:
        return 1
    return 1 + count_nodes(tree, tree[root][0]) + count_nodes(tree, tree[root][1])

print("Total number of nodes:", count_nodes(tree, root))

def count_leaves(tree, root):
    if not root:
        return 0
    if root not in tree:
        return 1
    if tree[root][0] is None and tree[root][1] is None:
        return 1
    return count_leaves(tree, tree[root][0]) + count_leaves(tree, tree[root][1])

print("Total number of leaves:", count_leaves(tree, root))

def count_internal_nodes(tree, root):
    if not root or root not in tree:
        return 0
    if tree[root][0] is None and tree[root][1] is None:
        return 0
    return 1 + count_internal_nodes(tree, tree[root][0]) + count_internal_nodes(tree, tree[root][1])

print("Total number of internal nodes:", count_internal_nodes(tree, root))

def search(tree, root, key):
    if not root:
        return False
    if root == key:
        return True
    if root not in tree:
        return False
    return search(tree, tree[root][0], key) or search(tree, tree[root][1], key)

key = input("Enter the node to search: ")
if search(tree, root, key):
    print(f"Node {key} found in the tree.")
else:
    print(f"Node {key} not found in the tree.")

def delete_node(tree, root, key):
    if root not in tree:
        return None
    left = tree[root][0]
    right = tree[root][1]
    if key < root:
        tree[root][0] = delete_node(tree, left, key)
    elif key > root:
        tree[root][1] = delete_node(tree, right, key)
    else:
        if left is None and right is None:
            del tree[root]
            return None
        elif left is None:
            del tree[root]
            return right
        elif right is None:
            del tree[root]
            return left
        temp = find_min(tree, right)
        tree[root][0], tree[root][1] = left, delete_node(tree, right, temp)
        tree[temp] = [left, right]
        del tree[root]
        return temp
    return root

def find_min(tree, root):
    while root in tree and tree[root][0]:
        root = tree[root][0]
    return root

key = input("Enter the node to delete: ")
delete_node(tree, root, key)
print("Updated Tree:")
for k, v in tree.items():
    print(k, ":", v)

def mirror(tree, root):
    if root in tree:
        tree[root][0], tree[root][1] = tree[root][1], tree[root][0]
        mirror(tree, tree[root][0])
        mirror(tree, tree[root][1])
    return tree

tree = mirror(tree, root)
print("\nMirrored Tree:")
for k, v in tree.items():
    print(k, ":", v)