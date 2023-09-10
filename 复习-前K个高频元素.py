import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 求元素频率
        freq_dict = {}
        for num in nums:
            freq_dict.setdefault(num, 0)
            freq_dict[num] += 1
        freq_heap = []
        for num, freq in freq_dict.items():
            heapq.heappush(freq_heap, (freq, num))
            if len(freq_heap) > k:
                heapq.heappop(freq_heap)
        result = []
        while len(freq_heap) > 0:
            result.append(heapq.heappop(freq_heap)[1])
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
