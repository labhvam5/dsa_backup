# initializing the list 
li = [1, -22, 43, 89, 2, 6, 3, 16] 
# li = [-22, 1, 2, 3, 6, 16, 43, 89]
n = len(li)

for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
        if li[j] < li[min_index]:
            min_index = j
            
        temp = li[i]
        li[i] = li[min_index]
        li[min_index] = temp

print(li)
