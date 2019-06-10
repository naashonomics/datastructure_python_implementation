def linear_search(array,key):
    pos=0
    found=False
    while pos < len(array) and not found:
            if array[pos] == key:
                found=True
            else:
                pos=pos+1
    return found
