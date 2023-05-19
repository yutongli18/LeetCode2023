"""
1016.子串能表示从1到N数字的二进制串
暴力方法会导致内存不足
关键在于想到n可以用2**k表示，进而和二进制串的长度产生联系，只查找部分长度的子串
"""
"""def toBinary(n):
    res = n
    binary = ""
    while res > 0:
        binary = str(res % 2) + binary
        res = int(res / 2)
    return binary"""


def check(k, s, mi, ma):
    length = ma - mi + 1
    subStringSet = set()
    sLength = len(s)
    for start in range(0, sLength-k+1):
        # print(s[start:start+k])
        binaryNum = int(s[start:start+k], base=2)
        if ma >= binaryNum >= mi:  # 不符合条件的子串值不能添加到set里
            subStringSet.add(binaryNum)
    # print(subStringSet)
    if len(subStringSet) >= length:
        return True
    else:
        return False


class Solution(object):
    def queryString(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: bool
        """
        """for num in range(1, n+1):
            # numBinary = toBinary(num)
            # if numBinary not in s:
                # return False
            numBinary = bin(num)
            if numBinary not in s:
                return False
        return True"""
        if n == 1:  # n=1
            if "1" not in s:
                return False
            else:
                return True
        k = 1
        while 2 ** k <= n:  # 找到k
            k += 1
        k -= 1
        # print(k)
        sLength = len(s)
        mi_1, ma_1 = 2 ** (k-1), 2 ** k - 1
        mi_2, ma_2 = 2 ** k, n
        if sLength < ma_1 - mi_1 + 1 or sLength < ma_2 - mi_2 + 1:  # 两个特殊条件
            # print("Here?")
            return False
        return check(k, s, mi_1, ma_1) and check(k+1, s, mi_2, ma_2)


if __name__ == '__main__':
    # print(toBinary(4))
    sol = Solution()
    print(sol.queryString(s="0110", n=3))
