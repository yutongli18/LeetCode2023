class Solution(object):
    def findAnagrams(self, s, p):
        """
        438.找到字符串中的所有字母异位词
        滑动窗口
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result_list = []
        a_code = ord('a')
        # 统计 p 中的字符出现情况
        p_dict = [0 for _ in range(26)]
        p_set = set()
        for i in range(len(p)):
            p_dict[ord(p[i]) - a_code] += 1
            p_set.add(p[i])
        # 用于匹配的字符频次列表
        map_dict = [num for num in p_dict]
        # 滑动窗口
        left, right = 0, 0
        while right < len(s):
            if s[right] not in p_set:
                # 如果当前滑动窗口内出现了不在 p 中的字符，直接跳过当前区间
                left = right + 1
                right = left
                map_dict = [num for num in p_dict]
                continue
            # 添加 s[right] 对应的字符
            map_dict[ord(s[right]) - a_code] -= 1
            while left <= right and map_dict[ord(s[right]) - a_code] < 0:
                map_dict[ord(s[left]) - a_code] += 1
                left += 1
            if left <= right and sum(map_dict) == 0:
                result_list.append(left)
            right += 1
        return result_list


if __name__ == "__main__":
    sol = Solution()
    print(sol.findAnagrams(s="abab", p="ab"))
