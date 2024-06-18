class BinaryListNode(object):
    def __init__(self, key=-1, value=-1, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next


class LRUCache(object):
    def __init__(self, capacity):
        """
        初始化
        包括键到节点指针的映射，双向链表的虚假头尾节点，容量
        :param capacity: int 容量
        """
        self.key_dict = {}
        self.head = BinaryListNode()
        self.tail = BinaryListNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = capacity

    def pop_head(self):
        """
        弹出第一个节点
        :return: BinaryListNode 第一个节点
        """
        node = self.head.next
        self.head.next = node.next
        node.next.pre = self.head
        node.pre = None
        node.next = None
        self.size += 1
        del self.key_dict[node.key]
        return node

    def pop_key(self, key):
        """
        弹出键为 key 的节点
        :param key: int 键
        :return: BinaryListNode 对应的节点
        """
        node = self.key_dict[key]
        node.pre.next = node.next
        node.next.pre = node.pre
        node.pre = None
        node.next = None
        self.size += 1
        del self.key_dict[key]
        return node

    def add_tail(self, key, value):
        """
        在尾节点前插入 (key, value) 节点
        :param key: int 键
        :param value: int 值
        :return: BinaryListNode 新插入的节点
        """
        node = BinaryListNode(key=key, value=value, pre=self.tail.pre, next=self.tail)
        self.tail.pre.next = node
        self.tail.pre = node
        self.size -= 1
        self.key_dict.setdefault(key, None)
        self.key_dict[key] = node
        return node

    def get(self, key):
        """
        返回键 key 对应的值
        :param key: int 键
        :return: int 对应的值
        """
        if self.key_dict.get(key):
            node = self.pop_key(key)
            self.add_tail(node.key, node.value)
            return node.value
        else:
            return -1

    def put(self, key, value):
        """
        插入 (key, value) 对
        :param key: int 键
        :param value: int 值
        :return: None
        """
        if self.key_dict.get(key):
            self.pop_key(key)
            self.add_tail(key, value)
        else:
            if self.size <= 0:
                self.pop_head()
            self.add_tail(key, value)


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
    lru.put(4, 4)
    print(lru.get(1))
    print(lru.get(3))
    print(lru.get(4))
