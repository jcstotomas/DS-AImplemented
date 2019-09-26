class Array:
    def __init__(self, size):
        self.size = size;
        self.array = [None] * size;
        self.hole = 0;

    def insert(self, val):
        if self.hole != self.size:
            self.array[self.hole] = val;
            self.hole += 1;

        else:
            print("full")


    def find(self,val):
        for i in range(self.size):
            if val == self.array[i]:
                return i;

        return -1;


    def delete(self, val):
        del_index = self.find(val)
        if del_index != -1:
            for i in range(del_index,self.size):
                if i != self.size - 1:
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
                else:
                    self.array[i] = None

            self.size -= 1;
        

array = Array(10);
array.insert(1)
array.insert(2)
array.insert(3)
array.insert(4)
array.insert(5)
array.insert(6)
array.insert(7)
array.insert(8)
array.insert(9)
array.insert(10)

print(array.array)

array.delete(1);
print(array.array)