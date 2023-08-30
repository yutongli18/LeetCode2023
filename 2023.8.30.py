"""
347.前 K 个高频元素
如何找到前 K 个高频元素，可以借助堆。
为了只对 K 个元素排序，降低时间复杂度，可以使用小顶堆。当堆中的数据超过 K 个时，将堆顶弹出。最后堆中剩下的元素就是结果。
（如果使用大顶堆，需要对所有不重复元素排序，再弹出堆顶 K 次，比小顶堆复杂）
"""


import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        """nums.sort()
        nums_counter = []
        prev = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == prev:
                count += 1
            else:
                nums_counter.append([prev, count])
                prev = nums[i]
                count = 1
        nums_counter.append([prev, count])
        nums_counter.sort(key=lambda x: x[1], reverse=True)
        result_list = []
        for i in range(k):
            result_list.append(nums_counter[i][0])
        return result_list"""
        nums_counter = {}
        for i in range(len(nums)):
            nums_counter.setdefault(nums[i], 0)
            nums_counter[nums[i]] += 1
        # 创建小顶堆
        min_heap = []
        for num, freq in nums_counter.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        # 输出前K个高频元素
        result_list = []
        for _ in range(k):
            result_list.append(heapq.heappop(min_heap)[1])
        return result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
