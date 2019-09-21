class Node:
    def __init__(self, value, next = None):
        self.next = next;
        self.value = value;
    
class LL:
    def __init__(self, head =None):
        self.head = head;

    def insert(self, value):
        self.head = Node(value,self.head)        

    def find(self, value):
        hP = self.head;
        while hP != None:
            if hP.value == value:
                return True;
            hP = hP.next;
        return False;

    def delete(self, value):
        previous = None;
        current = self.head;
        if current.value == value:
            self.head = self.head.next;
            return;
        while current != None:
            if current.value == value:
                previous.next = current.next

            else:
                previous = current;
                current = current.next;
                