class Solution(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        100367.切蛋糕的最小总开销 II
        贪心
        :type m: int
        :type n: int
        :type horizontalCut: List[int]
        :type verticalCut: List[int]
        :rtype: int
        """
        cost = 0
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        left, right = 0, 0
        h_count, v_count = 0, 0
        while left < len(horizontalCut) and right < len(verticalCut):
            if horizontalCut[left] >= verticalCut[right]:
                cost += horizontalCut[left] * (v_count + 1)
                h_count += 1
                left += 1
            else:
                cost += verticalCut[right] * (h_count + 1)
                v_count += 1
                right += 1
        if left < len(horizontalCut):
            while left < len(horizontalCut):
                cost += horizontalCut[left] * (v_count + 1)
                h_count += 1
                left += 1
        if right < len(verticalCut):
            while right < len(verticalCut):
                cost += verticalCut[right] * (h_count + 1)
                v_count += 1
                right += 1
        return cost


if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumCost(m=2, n=2, horizontalCut=[7], verticalCut=[4]))
