class Solution:
    def getPairCount(self, a, X):
        num_dict = {}
        for num in a:
            num_dict.setdefault(num, 0)
            num_dict[num] += 1
        # print(num_dict)
        count = 0
        for num in a:
            if (X - num) in num_dict.keys():
                count += num_dict[X - num]
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.getPairCount([1, 2, 3], 4))
