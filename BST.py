class TreeNode:
    def __init__(self, value =None, l=None, r=None):
        self.left = l;
        self.right = r;
        self.value = value


    def insert(self, value, root):

        if root == None:
            return TreeNode(value);

        if value > root.value:
            root.right = self.insert(value, root.right);
        else:
            root.left = self.insert(value, root.left);
                

        return root;
    def find(self, value, node):
        if node == None:
            return False;
        if value == node.value:
            return True;
        if value > node.value:
            return self.find(value,node.right);
        elif value < node.value:
            return self.find(value,node.left);

        return False;
            

    def inorder(self,root): 
        if root: 
            self.inorder(root.left) 
            print(root.value) 
            self.inorder(root.right)


    def findSuccessor(self, root):
        if root.right == None:
            return None;
        elif root.right != None:
            rootNode = root.right;
            predecessor = rootNode;
            while(rootNode != None):
                predecessor = rootNode;
                rootNode = rootNode.left;
        val = predecessor.value;
        predecessor = None;
        return val;

    def delete(self, value, node):
        if node == None:
            print("Not Found");
        elif node.value > value:
            delete(value, node.left);

        elif node.value < value:
            delete(value, node.right);
        elif node.value == value:
            if node.right != None and node.left != None:
                node.value = self.findSuccessor(node);
                
            if node.right != None and node.left == None || node.left != None and node.right == None:
                swap();            
            
class BinarySearchTree:
    def __init__(self, root):
        self.root = root;


root = TreeNode(1);

root.insert(10,root);
root.insert(0,root);
root.insert(-1,root);
root.insert(4,root);
root.insert(2,root);

root.inorder(root)
print(root.find(10,root));
print(root.findSuccessor(root));
root.delete(1, root);
root.inorder(root)
