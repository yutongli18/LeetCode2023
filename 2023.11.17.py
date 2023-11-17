"""
860.柠檬水找零
贪心法：5美元更万能，留在后面再消耗。
"""


class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        cash_count = {5: 0, 10: 0, 20: 0}
        for index in range(len(bills)):
            cash_count[bills[index]] += 1
            if bills[index] == 10:
                if cash_count[5] <= 0:
                    return False
                else:
                    cash_count[5] -= 1
            elif bills[index] == 20:
                if cash_count[10] > 0 and cash_count[5] > 0:
                    cash_count[10] -= 1
                    cash_count[5] -= 1
                elif cash_count[5] >= 3:
                    cash_count[5] -= 3
                else:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.lemonadeChange(bills=[5, 5, 10, 10, 20]))
