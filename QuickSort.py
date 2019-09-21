
def medianOfThree(array):
    first = array[0];
    last = array[-1];
    middle = array[len(array) // 2];
    median = None;
    if first > middle:
        if first < last:
            median = first;
        elif middle > last:
            median = middle;

        else:
            median = last;

    else:
        if first > last:
            median = first;

        elif middle < last:
            median= middle;

        else:
            median = last;
    
    if first == median:
        array[0], array[len(array) - 1] = array[len(array) - 1], array[0];

    elif middle == median:
        array[len(array) // 2], array[len(array) - 1] = array[len(array) - 1], array[len(array) // 2];

    return array;


def partition(array, start, end):
    array = medianOfThree(array);
    pivot = array[end];
    pIndex = start;
    end = end - 1;

    for i in range(end):
        if array[i] <= pivot:
            array[i], array[pIndex] = array[pIndex], array[i];
            pIndex+=1;

    array[end], array[pIndex] = array[pIndex], array[end];

    return pIndex, array;
        
    



    

def quickSort(array,start,end):
    if start < end:
        pI, array = partition(array,start,end);
        quickSort(array, start, pI-1);
        quickSort(array, pI + 1, end);

    print(array)


    

x = [20, 45, 21, 98, 19]
quickSort(x, 0, len(x));
