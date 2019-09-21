

class BinaryHeap:

    def __init__(self, a =[]):
        self.array = a;





    def percolateUp(self):
        i = len(self.array) - 1;

        while i // 2 > 0:
            if self.array[i] > self.array[i//2]:
                self.array[i], self.array[i//2] = self.array[i//2], self.array[i]


            i = i // 2;


    def insert(self, val):
        self.array.append(val);
        self.percolateUp();

        
    def print(self):
        print(self.array);


    def percolateDown(self, i):
        while i * 2 <= len(self.array):
            print(i)
            if self.array[i] < self.array[i+1]:
                self.array[i], self.array[i+1] = self.array[i+1], self.array[1];
            elif self.array[i] < self.array[i+2]:
                self.array[i], self.array[i+2] = self.array[i+2], self.array[1];
            i = i*2 +1;


    def delete(self):
        self.array[0], self.array[-1] = self.array[-1], self.array[0];
        self.array.pop();
        self.percolateDown(0);
    
        
                
                
        

testHeap = BinaryHeap([9, 5, 6, 2, 3])
testHeap.insert(7);
testHeap.print()
testHeap.delete();
testHeap.print();
