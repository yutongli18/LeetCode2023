class Solution(object):
    def doesAliceWin(self, s):
        """
        100335.字符串元音游戏
        :type s: str
        :rtype: bool
        """
        vowels = ["a", "e", "i", "o", "u"]
        # 先标记所有元音位置
        v_count = 0
        v_indices = [False for _ in range(len(s))]
        for i in range(len(s)):
            if s[i] in vowels:
                v_count += 1
                v_indices[i] = True
        # 轮流参与游戏
        role_odd = True
        is_removed = [False for _ in range(len(s))]
        while True:
            if role_odd:
                # 在小红的回合
                if v_count <= 0:
                    return False
                if v_count % 2 > 0:
                    return True
                i = 0
                while i < len(s) and v_count > 1:
                    if not is_removed[i]:
                        is_removed[i] = True
                        if s[i] in vowels:
                            v_count -= 1
                    i += 1
            else:
                # 在小明的回合
                if v_count % 2 == 0:
                    return False
                return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.doesAliceWin("bbcd"))
