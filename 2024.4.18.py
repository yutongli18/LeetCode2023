class Solution(object):
    def predictPartyVictory(self, senate):
        """
        649. Dota2 参议院
        应该优先消灭后面的参议员，因为前面的参议员已经行使过权利了，而后面的参议员依然有可能禁止己方成员的权利。
        :type senate: str
        :rtype: str
        """
        # 记录 D 和 R 的情况
        # 当出现 R 在 D 前面的情况时，flag + 1; D 在 R 前面时，flag - 1
        flag = 0
        # 布尔值，表示该阵营是否还有能够行使权利的参议员
        has_D, has_R = True, True
        # 布尔数组，表示该位置的参议员能否行使权利
        is_valid = [True for _ in range(len(senate))]
        while has_D and has_R:
            has_D, has_R = False, False
            # 如果有一个阵营没有成员了，就结束循环
            for i in range(len(senate)):
                # 如果该位置的成员已经在之前的轮次中被禁止了权利，就跳过
                if not is_valid[i]:
                    continue
                if senate[i] == 'R':
                    if flag < 0:
                        # 表示之前有 D，那么该参议员的权利会被禁止
                        is_valid[i] = False
                    else:
                        # 该参议员能够行使权利
                        has_R = True
                    flag += 1
                else:
                    if flag > 0:
                        is_valid[i] = False
                    else:
                        has_D = True
                    flag -= 1
        return 'Radiant' if has_R else 'Dire'


if __name__ == '__main__':
    sol = Solution()
    print(sol.predictPartyVictory(senate='DDRRR'))
