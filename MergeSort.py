
     


def split(array):
    ## finds the midpoint of the array
    midPoint = len(array) // 2;
    left = array[:midPoint];
    right = array[midPoint:]
    return left, right;





def mergeSort(array):
    if len(array) > 1:
        left, right = split(array);

        mergeSort(left);
        mergeSort(right);

        l = 0;
        r = 0;
        k = 0;
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                array[k] = left[l];
                l += 1;
            elif right[r] < left[l]:
                array[k] = right[r];
                r += 1;
            k+=1

        while l != len(left):
            array[k] = left[l];
            k += 1;
            l += 1;

        while r != len(right):
            array[k] = right[r]
            k += 1;
            r += 1;
            


x = [9,8,7,6,5,4,210]
mergeSort(x)
print(x)
