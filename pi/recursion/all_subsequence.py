# Print all the subsequence for an array in ordered format
def print_sub(index,res, arr, n):
    if index >= n:
        print(res)
        return
    res.append(arr[index])
    print_sub(index+1, res, arr, n)
    res.pop()
    print_sub(index+1, res, arr, n)

arr = [3,1,2]
print_sub(0, [], arr, len(arr))


# Print all the subsequences with the sum K 
def print_sub_k(index,res, arr, n, sum, k):
    if index >= n:
        # GEt the sum
        if sum == k:
            print(res)
        return

    res.append(arr[index])
    sum += arr[index]
    print_sub_k(index+1, res, arr, n, sum, k)
    sum -= arr[index]
    res.pop()
    print_sub_k(index+1, res, arr, n, sum, k)

arr = [3,1,2,5]
k = 5
print_sub_k(0, [], arr, len(arr), 0, 5)

#  Print only 1 subsequence with the sum K
def print_sub_bool(index,res, arr, n, sum, k)-> bool:
    if index >= n:
        # GEt the sum
        if sum == k:
            return True
        return False

    res.append(arr[index])
    sum += arr[index]
    if (print_sub_bool(index+1, res, arr, n, sum, k) == True):
        return True
    sum -= arr[index]
    res.pop()
    if (print_sub_bool(index+1, res, arr, n, sum, k) == True):
        return True
    return False

arr = [3,1,2,5]
k = 5
print_sub_bool(0, [], arr, len(arr), 0, 5)

# Print the number of occurances with the sum K
def print_sub_count(index, arr, n, sum, k)-> int:
    if index >= n:
        # GEt the sum
        if sum == k:
            return 1
        return 0

    sum += arr[index]
    l = print_sub_count(index+1, arr, n, sum, k)
    sum -= arr[index]
    r = print_sub_count(index+1, arr, n, sum, k)
    return l+r

arr = [3,1,2,5]
k = 5
print_sub_count(0, [], arr, len(arr), 0, 5)


# combination sum 1
def comb_sum(index, target, arr, n, res, ans):
    if index >=n:
        if target == 0:
            print(res)
            ans.append(list(res))
            print(ans)
        return

    if target >= arr[index]:
        res.append(arr[index])
        comb_sum(index, target - arr[index], arr, n, res, ans)
        res.pop()

    comb_sum(index+1, target, arr, n, res, ans)

ans= []
arr= [2,3,6,7]
target = 7
comb_sum(0, target, arr, len(arr), [], ans)
print(ans)


# combination Sum 2
def comb_sum(self, index, target, arr, n, res, ans):
    if target == 0:
        ans.append(list(res))
        return

    for x in range(index, n):
        if (arr[x] == arr[x-1] and x>index):
            continue
        if target < arr[x]:
            break
        res.append(arr[x])
        comb_sum(x+1, target - arr[x], arr, n, res, ans)
        res.pop()

arr= [1,1,1,2,2]
target = 4
ans= []
comb_sum(0, target, arr, len(arr), [], ans)
print(ans)


def comb_sum(index, target, arr, max_seq, res, ans):
    if index >= max_seq:
        if target == 0:
            ans.append(list(res))
            return
    
    if target == 0:
        ans.append(list(res))
        return
    # 0 1 2 3 4
    for x in range(index, max_seq):
        res.append(arr[x])
        comb_sum(index+1, target - arr[x], arr, max_seq, res, ans)
        res.pop()

arr= [1,2,3,4,5,6,7,8,9]
k = 3
target = 7
ans= []
max_seq = 4
comb_sum(0, target, arr, max_seq, [], ans)





