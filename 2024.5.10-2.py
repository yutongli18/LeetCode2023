class Solution(object):
    def groupAnagrams(self, strs):
        """
        49.字母异位词分组
        排序。
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 1:
            return [strs]
        sorted_strs = ["".join(sorted(list(string))) for string in strs]
        result_list = []
        group_map = {}
        for i in range(len(sorted_strs)):
            if group_map.get(sorted_strs[i], -1) == -1:
                result_list.append([strs[i]])
                group_map.setdefault(sorted_strs[i], len(result_list) - 1)
            else:
                result_list[group_map[sorted_strs[i]]].append(strs[i])
        return result_list


if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))
