class Solution(object):
    def findRepeatDocument(self, documents):
        """
        LCR 120.寻找文件副本
        :type documents: List[int]
        :rtype: int
        """
        n = len(documents)
        # 原地哈希
        i = 0
        while i < n:
            # 在 documents[i] 应该在的位置上已经有值了，并且在一个其它的索引位置上又出现了一个一样的值，说明发生了重复
            if documents[i] != i and documents[documents[i]] == documents[i]:
                return documents[i]
            if documents[documents[i]] != documents[i]:
                index = documents[i]
                documents[i], documents[index] = documents[index], documents[i]
            else:
                i += 1


if __name__ == "__main__":
    sol = Solution()
    print(sol.findRepeatDocument(documents=[2, 5, 3, 0, 5, 0]))
