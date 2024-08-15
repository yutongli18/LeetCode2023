class Solution(object):
    def decodeString(self, s):
        """
        394.字符串解码
        :type s: str
        :rtype: str
        """
        stack = []
        for ch in s:
            if ch == ']':
                sub_str = ''
                while stack[-1] != '[':
                    sub_str = stack.pop() + sub_str
                stack.pop()
                repeat = ''
                while stack and stack[-1].isdigit():
                    repeat = stack.pop() + repeat
                repeat = int(repeat)
                while repeat > 0:
                    stack.append(sub_str)
                    repeat -= 1
            else:
                stack.append(ch)
        decode = ''
        while stack:
            decode = stack.pop() + decode
        return decode


if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
