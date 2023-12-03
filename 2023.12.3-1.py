class Solution(object):
    def findPeaks(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        result_list = []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                result_list.append(i)
        return result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPeaks(mountain=[2, 4, 4]))
