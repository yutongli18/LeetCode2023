"""
22.括号生成
其实是产生一棵树的过程。
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(A):
            # print(A)
            if len(A) == 2 * n:
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append("(")  # 递归的产生左子树
                generate(A)
                A.pop()  # 回溯
                A.append(")")  # 递归的产生右子树
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for char in A:
                if char == "(":
                    bal += 1
                else:
                    bal -= 1
                if bal < 0:
                    return False
            return bal == 0

        ans = []
        generate([])
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(n=3))
