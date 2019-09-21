
class TreeNode:
    def __init__(self,value, left = None, right = None):
        self.right = right;
        self.left = left;
        self.value = value;

    def insertRight(self, value):
        self.right = TreeNode(value);

    def insertLeft(self, value):
        self.left = TreeNode(value);

    def removeRight(self):
        self.right = None;

    def removeLeft(self):
        self.left = None;

    def getValue(self):
        return self.value;

    
    
class BST:
    def __init__(self, root):
        self.root = root;


    def insert(self, value):
        newTreeNode = TreeNode(value);
                
