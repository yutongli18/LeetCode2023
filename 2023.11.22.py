class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        """result_list = []
        char_dict = {}
        for index in range(len(s)):
            char = s[index]
            char_dict.setdefault(char, [index, index])
            char_dict[char][1] = index
        index_list = list(char_dict.values())
        index_list.sort(key=lambda item: item[0])
        start, end = index_list[0][0], index_list[0][1]
        for i in range(1, len(index_list)):
            if index_list[i][0] > end:
                result_list.append(end - start + 1)
                start, end = index_list[i][0], index_list[i][1]
            else:
                end = max(end, index_list[i][1])
        result_list.append(end - start + 1)
        return result_list"""
        result_list = []
        char_dict = {}
        # 统计当前字母出现的最后位置
        for index in range(len(s)):
            char = s[index]
            char_dict.setdefault(char, index)
            char_dict[char] = index
        start, end = 0, 0
        for index in range(len(s)):
            char = s[index]
            end = max(end, char_dict[char])
            # 如果当前下标位置和之前出现字母的最远位置相等
            # 说明在当前下标位置分割，可以把之前所有出现的字母划分到一个片段中
            if index == end:
                result_list.append(end - start + 1)
                start, end = end + 1, end + 1
        return result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.partitionLabels(s="ababcbacadefegdehijhklij"))
