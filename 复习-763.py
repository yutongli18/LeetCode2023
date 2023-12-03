class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        char_dict = {}
        for i in range(len(s)):
            char_dict.setdefault(s[i], i)
            char_dict[s[i]] = i
        intervals = []
        start_i = 0
        max_i = -1
        for i in range(len(s)):
            max_i = max(max_i, char_dict[s[i]])
            if max_i == i:
                intervals.append(max_i - start_i + 1)
                start_i = max_i + 1
        return intervals


if __name__ == '__main__':
    sol = Solution()
    print(sol.partitionLabels(s="ababcbacadefegdehijhklij"))
