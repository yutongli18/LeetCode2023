class Solution(object):
    def gcd(self, a, b):
        """
        求 a 和 b 的最大公约数
        :type a: int
        :type b: int
        :rtype: int
        """
        if a < b:
            a, b = b, a
        divide, rest = a, b
        while True:
            new_rest = divide % rest
            if new_rest == 0:
                break
            divide = rest
            rest = new_rest
        return rest

    def minAnagramLength(self, s):
        """
        100283. 同位字符串连接的最小长度
        :type s: str
        :rtype: int
        """
        a_code = ord('a')
        # 统计 s 中所有字母的出现频率
        s_counter = [0 for _ in range(26)]
        for i in range(len(s)):
            s_counter[ord(s[i]) - a_code] += 1
        # 求所有字母出现频率的最大公约数（非零）
        s_gcd = 0
        for count in s_counter:
            if count == 0:
                continue
            if s_gcd == 0:
                s_gcd = count
            else:
                s_gcd = self.gcd(s_gcd, count)
        # 如果最大公约数是 1，那么只能把整个 s 字符串作为 t 了，因为无法分割
        if s_gcd == 1:
            return len(s)
        # 如果可能的话，在最大公约数的位置分割
        # 如果不能在最大公约数的位置分割，就往下找其因数
        # 枚举最大公约数的所有因数
        # 从大到小，方便求最小的 t
        gcd_division = []
        for i in range(s_gcd, 1, -1):
            if s_gcd % i == 0:
                gcd_division.append(i)
        # 依次检查每个因数能否作为分段数
        for division in gcd_division:
            splice_counter = [counter // division for counter in s_counter]
            splice_length = sum(splice_counter)
            # 依次检查每个分段
            i = 0
            while i < len(s):
                curr_counter = [counter for counter in splice_counter]
                is_valid = True
                for j in range(i, i + splice_length):
                    if curr_counter[ord(s[j]) - a_code] <= 0:
                        is_valid = False
                        break
                    curr_counter[ord(s[j]) - a_code] -= 1
                if not is_valid or sum(curr_counter) != 0:
                    break
                i += splice_length
            if i >= len(s):
                return splice_length
        # s_counter = [count // s_gcd for count in s_counter]
        # for i in range(len(s)):
        #     s_counter[ord(s[i]) - a_code] -= 1
        #     if sum(s_counter) == 0:
        #         return i - 0 + 1
        # return len(s)


if __name__ == "__main__":
    sol = Solution()
    print(sol.minAnagramLength(s="abba"))
