"""
1975.移除栅栏得到的正方形田地的最大面积
"""


class Solution(object):
    def get_distances(self, fences):
        distances = []
        for i in range(len(fences)):
            for j in range(i + 1, len(fences)):
                # 问题1：因为是距离，所以应该是绝对值
                distances.append(abs(fences[j] - fences[i]))
        # 问题2：距离不应该有重复
        return list(set(distances))

    def maximizeSquareArea(self, m, n, hFences, vFences):
        """
        :type m: int
        :type n: int
        :type hFences: List[int]
        :type vFences: List[int]
        :rtype: int
        """
        hFences += [1, m]
        vFences += [1, n]
        # 计算所有间距
        h_distances = self.get_distances(fences=hFences)
        v_distances = self.get_distances(fences=vFences)
        h_distances.sort()
        v_distances.sort()
        # 查找最大交集
        # 问题3：考虑到有可能不能组成正方形田地，所以应该赋值 -1
        max_distance = -1
        h_pointer, v_pointer = 0, 0
        while h_pointer < len(h_distances) and v_pointer < len(v_distances):
            if h_distances[h_pointer] == v_distances[v_pointer]:
                max_distance = max(max_distance, h_distances[h_pointer])
                # 问题4：即使是在满足条件的情况下，也应该让双指针自增，否则会陷入无限循环
                h_pointer += 1
                v_pointer += 1
            elif h_distances[h_pointer] > v_distances[v_pointer]:
                v_pointer += 1
            else:
                h_pointer += 1
        return (max_distance ** 2) % (10 ** 9 + 7) if max_distance > 0 else -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.maximizeSquareArea(m=4, n=3, hFences=[2, 3], vFences=[2]))
