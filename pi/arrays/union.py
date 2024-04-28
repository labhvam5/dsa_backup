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

    print(i, j)
    if i < n:
        for x in range(i,n):
            if val not in res:
                res.add(val)
    else:
        for x in range(j,m):
            if val not in res:
                res.add(val)
    
    return list(res)
