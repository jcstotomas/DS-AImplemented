class Node:
    def __init__(self, val, n =None):
        self.value = val;
        self.next = n;

    def getValue(self):
        return self.value;

    def setValue(self, val):
        self.value = val;

    def getNext(self):
        return self.next;

    def setNext(self, n):
        self.next = n;
        



class Stack:
    def __init__(self):
        self.head = None;

    def pop(self):
        x = self.head;
        self.head = self.head.getNext();
        return x;

    def push(self, val):
        x = Node(val, self.head);
        self.head = x;

    def peek(self):
        return self.head;

    def print(self):
        x = self.head
        while(x != None):
            print(x.getValue());
            x = x.getNext();
            


stack = Stack();

stack.push("hello");
stack.push("r");
stack.print();
stack.pop();
stack.print();
