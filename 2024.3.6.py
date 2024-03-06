"""
127.单词接龙
"""
from collections import deque


class Solution(object):
    def __init__(self):
        self.begin_word = ""
        self.end_word = ""
        self.word_list = set()
        # 是否已经遍历过
        self.visited = {}
        # 可以遍历的方向
        self.steps = 0
        # 可以改换的字母
        self.char_orders = 26

    def bfs_ladder(self):
        # 遍历长度
        length = 1
        queue = deque([self.begin_word])
        while queue:
            for _ in range(len(queue)):
                s_word = queue.popleft()
                for step in range(self.steps):
                    s_word_list = list(s_word)
                    for order in range(self.char_orders):
                        s_word_list[step] = chr(ord('a') + order)
                        new_word = ''.join(s_word_list)
                        if new_word in self.word_list and not self.visited[new_word]:
                            self.visited[new_word] = True
                            if new_word == self.end_word:
                                return length + 1
                            queue.append(new_word)
            length += 1
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # 初始化
        self.begin_word = beginWord
        self.end_word = endWord
        self.word_list = set(wordList)
        self.visited = {word: False for word in wordList}
        self.visited.setdefault(beginWord, True)
        self.steps = len(beginWord)
        # 排除
        if self.end_word not in self.word_list:
            return 0
        return self.bfs_ladder()


if __name__ == '__main__':
    sol = Solution()
    print(sol.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
