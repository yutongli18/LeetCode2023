class Solution:
    def binarySearch(self, n, m, k, start, end):
        if start >= end:
            return start
        mid = int((start + end) / 2)
        total_count = mid
        i = 1
        while i < k:
            curr_count = mid - (k - i)
            if curr_count < 1:
                curr_count = 1
            total_count += curr_count
            i += 1
        i = k + 1
        while i <= n:
            curr_count = mid - (i - k)
            if curr_count < 1:
                curr_count = 1
            total_count += curr_count
            i += 1
        if total_count == m:
            return self.binarySearch(n, m, k, mid, end)
        elif total_count < m:
            return self.binarySearch(n, m, k, mid + 1, end)
        else:
            return self.binarySearch(n, m, k, start, mid - 1)

    def getApples(self, n, m, k):
        return self.binarySearch(n, m, k, 1, m)


if __name__ == "__main__":
    sol = Solution()
    print(sol.getApples(n=4, m=9, k=4))
