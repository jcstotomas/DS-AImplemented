

class Queue:
    def __init__(self, size):
        self.size = size
        self.head = -1
        self.tail = -1
        self.array = [None] * self.size


    def enqueue(self,val):
        if (self.tail + 1 % self.size) == self.head:
            print("Full")
        elif (self.tail + 1) == 0:
            self.head = 0
            self.tail = 0
            self.array[self.tail] = val

        else:
            self.tail += 1
            self.array[self.tail] = val


    def dequeue(self):
        if self.head == -1:
            print("EMPTY")
        else:
            temp = self.head
            self.head = self.head + 1 % self.size
            print(self.array[temp])

    def print(self):
        print(self.array)

q = Queue(10)

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.print()
q.dequeue()
q.dequeue()