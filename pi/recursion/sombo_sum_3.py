class Solution:
    def comb_sum(self, index, target, arr, max_seq, k, res, ans):
        if target == 0:
            ans.append(list(res))
            return

        for x in range(index, max_seq):
            if index == 0 and x >= k-1:
                continue
            res.append(arr[x])
            self.comb_sum(x+1, target - arr[x], arr, max_seq, k, res, ans)
            res.pop()

    def combinationSum3(self, k: int, n: int):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        min_sum = 0
        max_sum = 0
        for i in range(k):
            min_sum += arr[i]
            max_sum += arr[len(arr) - i - 1]

        print(min_sum)
        print(max_sum)

        if n < min_sum or n > max_sum:
            return []

        max_seq = n - (min_sum - arr[k-1])
        print(max_seq)
        ans = []
        self.comb_sum(0, n, arr, max_seq, k, [], ans)
        return ans