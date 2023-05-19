"""
1105.填充书架
动态规划。
代码的难度在于，dp的下标从1开始，但是书的下标从0开始。
"""


class Solution(object):
    def minHeightShelves(self, books, shelfWidth):
        """
        :type books: List[List[int]]
        :type shelfWidth: int
        :rtype: int
        """
        booksLength = len(books)
        dp = [1000000 for _ in range(booksLength+1)]
        dp[0] = 0

        for i, book in enumerate(books):
            curWidth, maxHeight = 0, 0
            j = i
            while j >= 0:
                curWidth += books[j][0]
                if curWidth > shelfWidth:
                    break
                maxHeight = max(maxHeight, books[j][1])
                dp[i+1] = min(dp[i+1], dp[j] + maxHeight)
                j -= 1

        # print(dp)
        return dp[booksLength]


if __name__ == '__main__':
    sol = Solution()
    print(sol.minHeightShelves(books=[[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelfWidth=4))
