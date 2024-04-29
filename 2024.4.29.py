from collections import deque


class Solution(object):
    def __init__(self):
        # 起止单词
        self.begin_word = ''
        self.end_word = ''
        self.word_length = 0
        # 单词表
        self.word_set = set()
        # 遍历的方向
        self.a_code = ord('a')
        self.steps = 26
        # 是否已经遍历过
        self.visited = {}

    def word_bfs(self):
        queue = deque([self.begin_word])
        depth = 1
        while queue:
            layer_length = len(queue)
            for _ in range(layer_length):
                curr_word = queue.popleft()
                for i in range(self.word_length):
                    for step in range(self.steps):
                        new_word = curr_word[:i] + chr(self.a_code + step) + curr_word[i + 1:]
                        if new_word == self.end_word:
                            return depth + 1
                        if new_word in self.word_set and not self.visited[new_word]:
                            self.visited[new_word] = True
                            queue.append(new_word)
            depth += 1
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        """
        127.单词接龙
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        # 初始化
        self.begin_word = beginWord
        self.end_word = endWord
        self.word_length = len(beginWord)
        self.word_set = set(wordList)
        self.visited = {word: False for word in wordList}
        # BFS 求最短路径
        return self.word_bfs()


if __name__ == "__main__":
    sol = Solution()
    print(sol.ladderLength(beginWord='hit', endWord='cog', wordList=['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
