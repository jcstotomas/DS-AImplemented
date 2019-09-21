
class UnsortedArray:
    def __init__(self, size):
        self.size = size;
        self.array = [None] * self.size;
        self.current_hole = 0;
    def insert(self,item):
        self.array[self.current_hole] = item;
        self.current_hole += 1;

    def find(self,item):
        for i in range(self.size):
            if item == self.array[i]:
                return True;

        return False;

        



a = UnsortedArray(10);

a.insert(1);
a.insert(2)

print(a.find(2))