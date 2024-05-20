from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        239.滑动窗口最大值
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        # 单调递减的队列
        # 存放的是索引
        decrease_queue = deque([])
        for i in range(len(nums)):
            # 如果遇到了新的大值，就更新队列
            while len(decrease_queue) > 0 and nums[i] >= nums[decrease_queue[-1]]:
                decrease_queue.pop()
            decrease_queue.append(i)
            # 如果当前队列中最大值（队首）与当前索引的距离超过了 k，就弹出队首（它现在不在滑动窗口内了）
            if i - decrease_queue[0] >= k:
                decrease_queue.popleft()
            # 现在的队首就是滑动窗口内的最大值
            if i >= k - 1:
                result.append(nums[decrease_queue[0]])
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
