"""
2451.差值数组不同的字符串
我这里用了一个非常没有技术含量的算法。
difference1一定被先赋值。
"""


class Solution(object):
    def oddString(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        difference1, difference2 = [], []
        word1, word2 = "", ""
        choose = False
        for word in words:
            wordLength = len(word)
            difference = []
            for index in range(0, wordLength - 1):
                difference.append(ord(word[index + 1]) - ord(word[index]))
            if len(difference1) <= 0 and len(difference2) <= 0:
                difference1 = difference
                word1 = word
            elif difference != difference1:
                # 此时，如果difference2已经被赋值，difference1一定是那个特殊的
                # 如果difference2尚未赋值，考虑两种情况：
                # 第一种，difference1已经被重复，那么无须赋值，difference2一定是那个特殊的（通过choose来判断）
                # 第二种，difference1也只出现了一次，那么无法判断，只能先给difference2和word2赋值
                if len(difference2) <= 0:
                    if choose:
                        return word
                    difference2 = difference
                    word2 = word
                else:
                    return word1
            else:
                # 如果difference == difference1，考虑两种情况
                # 第一种，difference2已经被赋值，那么difference2一定是那个特殊的
                # 第二种，difference2尚未被赋值，但它一定是那个特殊的（参考上述第一种），给choose赋值来判断
                if len(difference2) > 0:
                    return word2
                else:
                    choose = True


if __name__ == '__main__':
    sol = Solution()
    print(sol.oddString(words=["adc", "wzy", "abc"]))
