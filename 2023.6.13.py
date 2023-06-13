from collections import Counter


class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsCounter = Counter(nums)
        count = 0
        numsSet = list(numsCounter.keys())
        for i in range(len(numsSet)):
            for j in range(i + 1, len(numsSet)):
                for k in range(j + 1, len(numsSet)):
                    count += numsCounter[numsSet[i]] * numsCounter[numsSet[j]] * numsCounter[numsSet[k]]
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.unequalTriplets(nums=[4, 4, 2, 4, 3]))
