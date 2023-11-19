class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        # 按照长度排序
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        if len(s2) < len(s3):
            s2, s3 = s3, s2
        if len(s1) < len(s3):
            s1, s3 = s3, s1
        count = 0
        index = 0
        for index in range(len(s3)):
            if s1[index] != s3[index] or s2[index] != s3[index]:
                if index < 1:
                    return -1
                count += max(0, len(s1) - index)
                count += max(0, len(s2) - index)
                count += max(0, len(s3) - index)
                return count
        count += max(0, len(s1) - (index + 1))
        count += max(0, len(s2) - (index + 1))
        count += max(0, len(s3) - (index + 1))
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.findMinimumOperations(s1="bcbb", s2="accbabb", s3="bcabb"))
