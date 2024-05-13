class Solution(object):
    def maximumEnergy(self, energy, k):
        """
        100274.从魔法师身上吸取的最大能量
        直接模拟？超时 => 倒着模拟
        动态规划？
        :type energy: List[int]
        :type k: int
        :rtype: int
        """
        # # 最大能量
        # max_energy = -1001 * len(energy)
        # # 到达第 i 个魔法师时能够获得的最大能量
        # dp = [max_energy for _ in range(len(energy))]
        # for i in range(len(energy)):
        #     dp[i] = max(energy[i], dp[i - k] + energy[i])
        #     if i + k >= len(energy):
        #         max_energy = max(max_energy, dp[i])
        # return max_energy

        total_energy = [energy[i] for i in range(len(energy))]
        for i in range(len(energy) - 1, -1, -1):
            total_energy[i] = total_energy[i] + total_energy[i + k] if i + k < len(energy) else total_energy[i]
        return max(total_energy)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumEnergy(energy=[-2, -3, -1], k=2))
