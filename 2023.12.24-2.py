"""
100169.移除栅栏得到的正方形田地的最大面积
暴力枚举。
"""


class Solution(object):
    def compute_distance(self, fences):
        fences.sort()
        distances = []
        for i in range(len(fences)):
            for j in range(i + 1, len(fences)):
                distances.append(fences[j] - fences[i])
        return list(set(distances))

    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        # 暴力枚举任意两个栅栏之间的距离
        hFences.extend([1, m])
        vFences.extend([1, n])
        h_distances = self.compute_distance(fences=hFences)
        v_distances = self.compute_distance(fences=vFences)
        # 查找交集，计算最大的正方形面积
        h_distances.sort()
        v_distances.sort()
        left, right = 0, 0
        max_edge = -1
        while left < len(h_distances) and right < len(v_distances):
            if h_distances[left] == v_distances[right]:
                max_edge = max(max_edge, h_distances[left])
                left += 1
                right += 1
            elif h_distances[left] < v_distances[right]:
                left += 1
            else:
                right += 1
        return max_edge ** 2 % (10 ** 9 + 7) if max_edge != -1 else -1
        """cover_distances = h_distances & v_distances
        if cover_distances:
            ans = max(cover_distances)
        else:
            ans = 0
        return ans ** 2 % (10 ** 9 + 7) if ans else -1"""


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximizeSquareArea(m=6, n=7, hFences=[2], vFences=[4]))
