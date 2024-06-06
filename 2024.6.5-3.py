class Solution:
    def get_max(self, seqs):
        """
        来自于同一个媒体源的最大媒体包个数
        不同媒体源之间的包可能混杂在一起
        :param seqs: 媒体包序列号列表 [int]
        :return: 最大媒体包个数 int
        """
        MAX_SEQ = 65536
        # 不同的媒体源 {pre_seq: length}
        sources = {}
        # 遍历媒体包列表
        for seq in seqs:
            if len(sources) <= 0:
                sources[seq] = 1
            step = 1
            while step <= 11:
                pre_seq = ((seq - step) + MAX_SEQ) % MAX_SEQ
                # 尽可能选紧挨着的？
                if sources.get(pre_seq) and sources.get(pre_seq) != 0:
                    sources[seq] = sources[pre_seq] + 1
                    sources[pre_seq] = 0
                    break
                step += 1
            if step > 11:
                sources[seq] = 1
        # print(sources)
        return max(sources.values())


if __name__ == '__main__':
    n = input()
    seqs = [int(seq) for seq in input().split(" ")]
    # print(seqs)
    sol = Solution()
    print(sol.get_max(seqs=seqs))
