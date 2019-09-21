
# def binary_search(a, find_item):
#     start = 0;
#     end = len(a) - 1;

#     while start <= end:
#         mid = start + (end - start) // 2;

#         if a[mid] == find_item:
#             return True;
        
#         if a[mid] > find_item:
#             end = mid - 1;
#         else:
#             start = mid + 1;
#     return False

def binary_search(a, find):
    start = 0;
    end = len(a) - 1;

    while start <= end:
        mid = start + (end-start) // 2;

        if a[mid] == find:
            return True;
        if a[mid] > find:
            end = mid - 1;
        else:
            start = mid + 1;
    return False;
a = [1,2,4,5,6,7,8,9,10,11]

print(binary_search(a,1))