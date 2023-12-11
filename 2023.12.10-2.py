class Solution(object):
    def getGoodIndices(self, variables, target):
        """
        :type variables: List[List[int]]
        :type target: int
        :rtype: List[int]
        """
        result_list = []
        for i in range(len(variables)):
            a, b, c, m = variables[i]
            if (a ** b % 10) ** c % m == target:
                result_list.append(i)
        return result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.getGoodIndices(variables=[[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], target=2))
