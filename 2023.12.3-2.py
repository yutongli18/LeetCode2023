"""
100153.需要添加的硬币的最小数量
① 如何判断能构成的所有金额？ => 分类讨论，找上限
② 知道还缺少哪些金额之后，如何添加硬币，使得添加的硬币数最少，但是能满足条件？ => 不需要知道还缺少哪些金额，知道目前能凑出来的上限即可
"""


class Solution(object):
    def minimumAddedCoins(self, coins, target):
        """
        :type coins: List[int]
        :type target: int
        :rtype: int
        """
        coins.sort()
        # 需要添加的硬币数
        count = 0
        # 遍历硬币的索引
        i = 0
        # 上限，目前可取得的金额范围为：[0, s-1]
        s = 1
        while s <= target:
            if i < len(coins) and coins[i] <= s:
                # 更新目前可取得的金额范围为：[0, s + x - 1]
                s += coins[i]
                i += 1
            else:
                # 为了能够达到 target 必须添加一枚面值为 s 的硬币
                count += 1
                # 更新目前可取得的金额范围为：[0, 2 * s - 1]
                s *= 2
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumAddedCoins(coins=[1, 4, 10, 5, 7, 19], target=19))
