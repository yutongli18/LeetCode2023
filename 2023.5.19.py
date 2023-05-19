"""
1079.活字印刷
DFS遍历
"""


from collections import Counter


def dfs(i, sentenceSet, counter):
    if i == 0:
        # print("返回")
        return 1
    res = 1
    for tile in sentenceSet:
        if counter[tile] > 0:
            counter[tile] -= 1
            res += dfs(i-1, sentenceSet, counter)
            counter[tile] += 1  # 回溯
    return res


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        counter = Counter(tiles)
        sentenceSet = set(tiles)
        return dfs(len(tiles), sentenceSet, counter) - 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.numTilePossibilities(tiles="AAB"))
