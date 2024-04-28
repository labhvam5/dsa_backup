import sys
sys.stdout = open('/home/labhvam5/Documents/dsa_backup/output.txt', 'w')
sys.stdin = open('/home/labhvam5/Documents/dsa_backup/input.txt', 'r')

x = int(input())
y = int(input())

def check_if_duplicates(arr):
    if len(arr) == len(set(arr)):
        return False
    else:
        return True


def print_sub(index,res, arr, n):
    if index >= n:
        if check_if_duplicates(res):
            return
        else:
            count= count+1
            return

    res.append(arr[index])
    print_sub(index+1, res, arr, n)
    res.pop()
    print_sub(index+1, res, arr, n)

arr = [0,1,1,1]
print_sub(0, [], arr, len(arr))
