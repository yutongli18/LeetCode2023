"""
100251.数组中的最短非公共子字符串
"""


class Solution(object):
    def substring_set(self, arr):
        substrings = []
        for start in range(len(arr)):
            for step in range(len(arr) - start):
                substrings.append(arr[start:start + step + 1])
        substrings.sort(key=lambda item: (len(item), item))
        return substrings

    def shortestSubstrings(self, arr):
        """
        :type arr: List[str]
        :rtype: List[str]
        """
        # 求子字符串集合
        arr_dict = []
        for i in range(len(arr)):
            arr_dict.append(self.substring_set(arr[i]))
        # 求 answer
        answer = []
        for i in range(len(arr)):
            for sub_s in arr_dict[i]:
                check_point = 0
                for j in range(len(arr)):
                    if j != i and sub_s not in arr_dict[j]:
                        check_point += 1
                if check_point >= len(arr) - 1:
                    answer.append(sub_s)
                    break
            if len(answer) < i + 1:
                answer.append("")
        return answer


if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestSubstrings(arr=["cab", "ad", "bad", "c"]))
