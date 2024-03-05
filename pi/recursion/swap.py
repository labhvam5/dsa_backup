# Reverse an array using recursion 
def rev(i, arr, n):
    if i > n/2:
        return
    temp = arr[i]
    arr[i]= arr[n-i]
    arr[n-i]= temp
    rev(i+1, arr, n)

arr = [1,2,3,8,10]
print(arr)
rev(0, arr, len(arr)-1)
print(arr)

# Check if a string is palindrome or not using recursion
def check(i, s, n):
    if i > n/2:
        return True
    if s[i] != s[n-i]:
        return False
    return check(i+1, s, n)

s = "madam"
print(check(0, s, len(s)))