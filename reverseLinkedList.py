
class Node:
    def __init__(self, value, n= None):
        self.next = n;
        self.value = value;



class LL:

    def __init__(self, head):
        self.head = head;

    def returnHead(self):
        return self.head


    def insert(self, value):
        newHead = Node(value,self.head)
        self.head = newHead;


    def print(self):
        h = self.head;

        while h != None:
            print(h.value)
            h = h.next;


def reverseLL(ll):
    previous = None;
    current = ll
    n = None

    while current != None:
        n = current.next;
        current.next = previous;
        previous = current;

        current = n;


    return previous

newNode = Node("A");

LinkedList = LL(newNode)

        
LinkedList.insert("B");
LinkedList.insert("C");

LinkedList.print()

x = LL(reverseLL(LinkedList.returnHead()));


x.print()





    

