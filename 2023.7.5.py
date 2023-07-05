"""
904.水果成篮
滑动窗口：处理连续数组问题。
编程过程中遇到的两个问题：
① 对测试案例[0,1,1,4,3]：无论当前滑动窗口的左边界是否发生了移动，右边界位置的水果都需要采摘，所以fruitSet.append(fruits[end])不能放在判断条
件里面，否则上述案例中的水果种类 4 会被直接跳过。
② 对测试案例 [3,3,3,1,2,1,1,2,3,3,4]：如果用 index 直接跳转，index 需要记录最后一次水果种类发生变化的位置，否则对于 12112 这个序列，当遍历
到水果种类 3 时，index 会跳转到第一个 2 出现的位置，此时再采摘 3 ，会同时采摘 3 种种类的水果。这里还需要处理应该把哪种水果抛出集合 fruitSet的问
题，直接把 index - 1 位置的水果种类抛出即可，因为 index 位置表示水果种类发生变化的位置。
"""


class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        result = 0
        n = len(fruits)
        fruitSet, index = [], -1  # 记录已经挑选过的水果种类和上次水果种类发生变化的位置（调整滑动窗口左边界用）
        start, end = 0, 0  # 滑动窗口的左右边界
        while end < n:
            if fruits[end] not in fruitSet:
                # print(fruits[end])
                # print(fruitSet)
                if len(fruitSet) == 2:  # 已经有两种水果了
                    result = max(result, end - start)  # 当前次采摘完毕
                    start = index  # 滑动窗口移动到上次水果种类发生变化的位置
                    fruitSet.remove(fruits[index - 1])  # 下一轮开始时，不采摘前一种水果了
                # 无论滑动窗口的左边界是否会发生变化，当前位置的水果都要采摘
                fruitSet.append(fruits[end])
            if fruits[end] != fruits[end - 1]:  # 只要水果种类发生变化，index的坐标位置就发生变化，以此记录最近的一次变化
                index = end
            end += 1
            # print(fruitSet)
        result = max(result, end - start)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.totalFruit(fruits=[0, 1, 1, 4, 3]))
