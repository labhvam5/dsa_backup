def longestSubarrayWithSumK(a: [int], k: int) -> int:
    n = len(a)
    max_len = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += a[j]
            if sum > k:
                break;
            elif sum == k and max_len < ((j-i)+1):
                max_len = (j-i)+1
    
    return max_len
