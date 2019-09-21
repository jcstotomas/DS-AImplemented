def hashFunction(string, length):
    return hash(string) % length


class ListNode:
    def __init__(self, val=None, n = None):
        self.value = val;
        self.ne = n;


class LinkedList:
    def __init__(self, head = None):
        self.head = head;

    def search(self,val):
        ll = self.head
        while (ll != None):
            if ll.value == val:
                return True;
            ll = ll.ne;
        return False

    def insert(self, val):
        self.head = ListNode(val, self.head);

    def remove(self,val):
        ll = self.head;
        previous = None
        if ll.value == val:
            self.head = ll.ne;
        else:
            while(ll != None):
                if ll.value == val:
                    previous.ne = ll.ne;
                    break;
                previous = ll;
                ll = ll.ne
        
    def print(self):
        ll = self.head;
        while (ll != None):
            print(ll.value);
            ll = ll.ne;

                
        

class HashTable:
    def __init__(self, length):
        self.array = [None] * length;
        for i in range(len(self.array)):
            self.array[i] = LinkedList();
        self.length = length
        print(self.array);

    def insert(self, string):
        currentBucket = self.array[hashFunction(string,self.length)].insert(string);

    def print(self):
        for i in self.array:
            i.print();

x = HashTable(2);
x.insert("hello");
x.insert("a");
x.print()    
    
    
