class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = {}
        # 确定当前节点是否为根节点
        self.is_end = False


class Trie(object):
    def __init__(self):
        self.head = TreeNode("")

    def insert(self, word):
        """
        向前缀树中插入字符串word
        :param word: String
        :return: None
        """
        word_list = list(word)
        pointer = self.head
        for ch in word_list:
            if pointer.children.get(ch):
                pointer = pointer.children[ch]
            else:
                node = TreeNode(ch)
                pointer.children[ch] = node
                pointer = node
        pointer.is_end = True

    def search_prefix(self, prefix):
        """
        检索前缀
        :param prefix: String
        :return: TreeNode
        """
        word_list = list(prefix)
        pointer = self.head
        for ch in word_list:
            if pointer.children.get(ch):
                pointer = pointer.children[ch]
            else:
                return None
        return pointer

    def search(self, word):
        node = self.search_prefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix):
        node = self.search_prefix(prefix)
        return node is not None


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
