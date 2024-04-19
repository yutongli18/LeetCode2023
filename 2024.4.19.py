class Solution(object):
    def balancedStringSplit(self, s):
        """
        1221. 分割平衡字符串
        :type s: str
        :rtype: int
        """
        substring_count = 0
        start = 0
        RL_count = {'R': 0, 'L': 0}
        for end in range(len(s)):
            RL_count[s[end]] += 1
            if RL_count['R'] == RL_count['L']:
                substring_count += 1
                start = end
        return substring_count


if __name__ == '__main__':
    sol = Solution()
    print(sol.balancedStringSplit(s='LLLLRRRR'))
