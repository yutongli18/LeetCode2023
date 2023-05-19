"""
1054.距离相等的条形码
靠原地换位会出现一个问题：当最后两个条形码相等的时候，对于最后一个条形码，找不到能和它交换的其它条形码了，往前换可能会破坏已经整理好的部分。
所以最好是对整个数组中的元素进行重新排布。
如何快速地找到每个回合里面，出现频次最大的条形码？ =》 堆
"""


from collections import Counter
import heapq


class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        counter = Counter(barcodes)
        # print(counter)
        q = []
        for barcode, count in counter.items():
            heapq.heappush(q, (-count, barcode))
        newBarcodes = []
        while len(q) > 0:
            count, barcode = heapq.heappop(q)
            if len(newBarcodes) == 0 or newBarcodes[-1] != barcode:
                newBarcodes.append(barcode)
                if count < -1:
                    heapq.heappush(q, (count + 1, barcode))
            else:
                count_2, barcode_2 = heapq.heappop(q)
                heapq.heappush(q, (count, barcode))
                newBarcodes.append(barcode_2)
                if count_2 < -1:
                    heapq.heappush(q, (count_2 + 1, barcode_2))
        return newBarcodes


if __name__ == '__main__':
    sol = Solution()
    print(sol.rearrangeBarcodes(barcodes=[1, 1, 1, 2, 2, 2]))
    # sol.rearrangeBarcodes(barcodes=[1, 1, 1, 2, 2, 2])
