# initializing the list 
li = [1, -22, 43, 89, 2, 6, 3, 16] 
li = [-22, 1, 2, 3, 6, 16, 43, 89]
n = len(li)

for i in range(n-1):
    print("labhvam")
    swapped = False
    for j in range(n-1-i):
        if li[j] > li[j+1]:
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp
            swapped = True
    
    if swapped == False:
        break

print(li)