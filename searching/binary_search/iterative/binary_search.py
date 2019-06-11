def binary_search(array,key):
    low=0
    high= len(array)-1
    while low <= high:
        mid=(low+high)//2
        if key==array[mid]:
            return True
        elif key < array[mid]:
            high = mid-1
        else:
            low=mid+1
    return False