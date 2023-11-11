class Solution(object):
    def __init__(self):
        self.result_list = []
        self.curr_result = []

    def check_palindromic(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def get_partition(self, sub_s):
        if not sub_s:
            self.result_list.append(self.curr_result[:])
            return
        for index in range(1, len(sub_s) + 1):
            left_s = sub_s[:index]
            right_s = sub_s[index:]
            if not self.check_palindromic(left_s):
                continue
            self.curr_result.append(left_s[:])
            self.get_partition(right_s[:])
            self.curr_result.pop(-1)

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.get_partition(sub_s=s[:])
        return self.result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.partition(s="google"))
