"""
100258.最高频率的 ID
最大堆
"""


import heapq


class Solution(object):
    def mostFrequentIDs(self, nums, freq):
        """
        :type nums: List[int]
        :type freq: List[int]
        :rtype: List[int]
        """
        # answer = [0 for _ in range(len(nums))]
        # set_dict = {}
        # for i in range(len(nums)):
        #     set_dict.setdefault(nums[i], 0)
        #     set_dict[nums[i]] += freq[i]
        #     for value in set_dict.values():
        #         answer[i] = max(answer[i], value)
        # return answer
        # 最大堆
        answer = []
        set_dict = {}
        heap = []
        for i in range(len(nums)):
            set_dict.setdefault(nums[i], 0)
            set_dict[nums[i]] += freq[i]
            heapq.heappush(heap, (-set_dict[nums[i]], nums[i]))
            while heap and -heap[0][0] != set_dict[heap[0][1]]:
                heapq.heappop(heap)
            answer.append(-heap[0][0])
        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.mostFrequentIDs(nums=[2, 3, 2, 1], freq=[3, 2, -3, 1]))
