"""
93. 复原 IP 地址
和分割回文串本质上是一样的，只不过这次的串还加了一个必须分为四组的条件限制，可以作为终止条件了。
"""


class Solution(object):
    def __init__(self):
        self.result_list = []
        self.curr_result = []

    def check_ip_bit(self, ip_bit):
        """
        检查当前这一位（子串）是否满足 IP 地址中一位的条件
        :param ip_bit: string
        :return: bool
        """
        # 这里：考虑到单独一个 “0” 的情况也合法，这时候第一位是 “0”，但是不是前导零。
        if len(ip_bit) > 1 and ip_bit[0] == "0":  # 不能有前导零
            return False
        ip_bit_num = int(ip_bit)
        if ip_bit_num > 255:  # 在 0~255 之间取值
            return False
        return True

    def build_ip_address(self, s):
        """
        用回溯法构建 IP 地址
        :param s: string，当前子串
        :return: None
        """
        if len(self.curr_result) == 4:
            if not s:  # 正好构成了一个 IP 地址
                self.result_list.append(".".join(self.curr_result))
            return
        for split_index in range(1, len(s) + 1):
            s_left, s_right = s[:split_index], s[split_index:]
            if len(s_right) > (4 - len(self.curr_result)) * 3:
                continue
            if not self.check_ip_bit(s_left):
                continue
            self.curr_result.append(s_left)
            self.build_ip_address(s_right)
            self.curr_result.pop(-1)

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.build_ip_address(s)
        return self.result_list


if __name__ == '__main__':
    sol = Solution()
    print(sol.restoreIpAddresses(s="25525511135"))
