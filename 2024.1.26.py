"""
496.下一个更大元素 I
"""


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 从 nums2 上求单调栈
        ans = {}
        stack = []
        for i in range(len(nums2)):
            ans.setdefault(nums2[i], -1)
            while stack and nums2[stack[-1]] < nums2[i]:
                index = stack.pop(-1)
                ans[nums2[index]] = nums2[i]
            stack.append(i)
        # 获取结果
        result = [-1 for _ in range(len(nums1))]
        for i in range(len(nums1)):
            result[i] = ans[nums1[i]]
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
