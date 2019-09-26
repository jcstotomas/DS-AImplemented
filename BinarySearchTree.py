class TreeNode:
    def __init__(self, val,l = None, r = None):
        self.left = l
        self.right = r
        self.value = val


def insert(root, val):
    node = TreeNode(val)
    if root == None:
        root = node
    
    else:
        if val > root.value:
            if root.right == None:
                root.right = node
            else:
                insert(root.right, val)

        else: 
            if root.left == None:
                root.left = node
            else:
                insert(root.left, val)
    
def findSuccessor(root):
    current = root.right;
    while (current.left != None):
        current = current.left;
    return current

def remove(root, val):
    if root == None:
        root = None
    else:
        if root.value < val:
            remove(root.right, val)
        elif root.value > val:
            remove(root.left, val)
        else:
            if root.left != None and root.right != None:
                successor = findSuccessor(root)
                root.value = successor.value
                remove(root.right, root.value)
            elif root.left == None and root.right != None:
                root.value = root.right.value
                root.right = None;
            
            elif root.left != None and root.right == None:
                root.value = root.left.value
                root.left = None
            
            else:
                root = None
                return
            return

def printTree(root):
    if root != None:
        printTree(root.left)
        print(root.value)
        printTree(root.right)

BST = TreeNode(6)

insert(BST, 4)
insert(BST, 7)
insert(BST, 9)
insert(BST, 3)
insert(BST, 5)
insert(BST, 8)
insert(BST, 1)

printTree(BST)

print("remove")
remove(BST,8)
printTree(BST)