def binary_search(arr, l, r, n):
    while(l <= r):
        mid = l + ((r - l)/2)

        if arr[mid] == n:
            return mid
        
        elif arr[mid] < n:
            l = mid+1
        else:
            r = mid-1
        
    return -1

