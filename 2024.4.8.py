class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        925. 长键键入
        :type name: str
        :type typed: str
        :rtype: bool
        """
        left, right = 0, 0
        while left < len(name) and right < len(typed):
            # 如果当前位相等就继续向下比较
            if name[left] == typed[right]:
                left += 1
                right += 1
            else:
                # 如果当前位不相等
                # 首先，跳过长键键入的部分
                while 0 < right < len(typed) and typed[right] == typed[right - 1]:
                    right += 1
                # 如果跳过长键键入的部分之后还是不相等，说明不匹配
                if right >= len(typed) or name[left] != typed[right]:
                    return False
                else:
                    left += 1
                    right += 1
        # 比较完成后，如果 name 没有匹配完，说明不匹配
        if left < len(name):
            return False
        # 如果 typed 没有匹配完，先把长键键入的部分跳过
        while right < len(typed) and typed[right] == typed[right - 1]:
            right += 1
        # 如果在长键键入的后面还有不同的字母，说明不匹配
        if right < len(typed):
            return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isLongPressedName(name="kikcxmvzi", typed="kiikcxxmmvvzz"))
