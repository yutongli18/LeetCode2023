class Solution(object):
    def setZero(self, string):
        change_steps = []
        string_list = [int(ch) for ch in string]
        if (len(string_list) - sum(string_list)) % 2 != 0:
            return -1
        left, right = 0, 1
        while right < len(string_list):
            while string_list[left] != 0 and left < len(string_list):
                left += 1
            if left >= len(string_list):
                return change_steps
            right = left + 2
            while string_list[right] != 0 and right < len(string_list):
                right += 1
            if right >= len(string_list):
                return -1
            string_list[left] = 1
            string_list[right] = 1
            change_steps.append([left + 1, right + 1])
            left += 1
            right += 1
        return change_steps


if __name__ == '__main__':
    sol = Solution()
    string = input()
    change_steps = sol.setZero(string)
    print(len(change_steps))
    for (left, right) in change_steps:
        print(left, right)
