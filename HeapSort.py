


def percolateUp(heap):
    i = len(heap) - 1;
    while i//2 > 0:
        parent = i // 2;
        if heap[i] <= heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i];
        i = i // 2;
        
    return heap;
    
    
def percolateDown(heap):
    for i in range(len(heap)):
        currentNode = i;
        left = 2*i + 1;
        right = 2*1 + 2;

        if left < len(heap) and heap[currentNode] >= heap[left]:  
            heap[left], heap[currentNode] = heap[currentNode], heap[left];

        elif right < len(heap) and heap[currentNode] >= heap[right]:
            heap[right], heap[currentNode] = heap[currentNode], heap[right];
        
    return heap;

sample = [0,5,4,3,2,1]



print(percolateUp(sample))
