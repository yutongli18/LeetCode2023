"""
38.外观数列
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = ""
        for i in range(n):
            if i == 0:
                result = "1"
            else:
                current, newResult = "", ""
                count = 0
                for char in result:
                    if len(current) <= 0:
                        current = char
                        count = 1
                    else:
                        if char != current:
                            newResult += str(count) + current
                            current = char
                            count = 1
                        else:
                            count += 1
                newResult += str(count) + current
                result = newResult
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.countAndSay(n=4))
