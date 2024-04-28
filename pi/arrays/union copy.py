a = [1,2,3,4,6]
b = [2,3,5]

def sortedArray(a: [int], b: [int]) -> [int]:
    i = 0
    j = 0
    n = len(a)
    m = len(b)
    res = set()
    
    while i<n and j<m:
        if a[i] <= b[j]:
            val = a[i]
            i = i+1
        else:
            val = b[j]
            j = j+1
        
        if val not in res:
            res.add(val)
    
    while i < n:  # If any elements left in arr1
        if a[i] not in res:
            res.add(a[i])
        i += 1

    while j < m:  # If any elements left in arr2
        if b[j] not in res:
            res.add(b[j])
        j +=1
    
    return list(res)
