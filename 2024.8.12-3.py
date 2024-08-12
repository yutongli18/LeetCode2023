import time


class ListNode:
    def __init__(self, key="", value="", timestamp=None, pre=None, post=None):
        self.key = key
        self.value = value
        self.timestamp = timestamp if timestamp else time.time()
        self.pre = pre
        self.post = post


class LRU:
    def __init__(self, maxSize, maxAge=None):
        self.key_map = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.post = self.tail
        self.tail.pre = self.head
        self.size = maxSize
        self.maxSize = maxSize
        # 毫秒转换成秒
        self.maxAge = maxAge // 1000 if maxAge else 1e+308

    def pop_head(self):
        temp = self.head.post
        if temp == self.tail:
            return None
        self.head.post = temp.post
        temp.post.pre = self.head
        temp.pre = None
        temp.post = None
        self.key_map[temp.key] = None
        self.size += 1
        return temp

    def pop_key(self, key):
        temp = self.key_map.get(key)
        if not temp:
            return None
        temp.pre.post = temp.post
        temp.post.pre = temp.pre
        temp.pre = None
        temp.post = None
        self.key_map[key] = None
        self.size += 1
        return temp

    def add_tail(self, key, value, timestamp):
        node = ListNode(key, value, timestamp, self.tail.pre, self.tail)
        self.tail.pre.post = node
        self.tail.pre = node
        self.key_map.setdefault(key, None)
        self.key_map[key] = node
        self.size -= 1

    def get(self, key):
        now = time.time()
        temp = self.pop_key(key)
        if not temp or now - temp.timestamp > self.maxAge:
            return None
        self.add_tail(key, temp.value, now)
        return temp.value

    def set(self, key, value):
        now = time.time()
        self.pop_key(key)
        while self.size <= 0:
            self.pop_head()
        self.add_tail(key, value, now)

    def keys(self):
        now = time.time()
        temp = self.head.post
        while temp != self.tail:
            if now - temp.timestamp > self.maxAge:
                self.pop_head()
                temp = self.head.post
            else:
                break
        return list(reversed(self.key_map.keys()))

    def sleep(self, t):
        # 毫秒转换成秒
        time.sleep(t // 1000)


if __name__ == "__main__":
    lru = LRU(10, 5000)
    lru.set("element1", "bar")
    lru.sleep(3000)
    lru.set("element2", "foo")
    print(lru.get("element2"))
    print(lru.keys())
    lru.sleep(3000)
    print(lru.get("element1"))
