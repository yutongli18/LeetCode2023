class Solution(object):
    def getIndex(self, s, sub):
        """
        返回所有的子串位置。
        :param s: str
        :param sub: str
        :return: List[int]
        """
        indices = []
        start = 0
        while start + len(sub) - 1 < len(s):
            index = s.find(sub, start)
            if index == -1:
                break
            indices.append(index)
            start = index + len(sub)
        return indices

    def beautifulIndices(self, s, a, b, k):
        """
        :type s: str
        :type a: str
        :type b: str
        :type k: int
        :rtype: List[int]
        """
        i_index = self.getIndex(s=s, sub=a)
        j_index = self.getIndex(s=s, sub=b)
        print(i_index, j_index)
        result_index = []
        i_p, j_p = 0, 0
        while i_p < len(i_index) and j_p < len(j_index):
            if i_index[i_p] - k <= j_index[j_p] <= i_index[i_p] + k:
                result_index.append(i_index[i_p])
                i_p += 1
            elif j_index[j_p] < i_index[i_p]:
                j_p += 1
            else:
                i_p += 1
        return result_index


if __name__ == '__main__':
    sol = Solution()
    print(sol.beautifulIndices(s="ocmm", a="m", b="oc", k=15))
