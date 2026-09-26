class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = Node()
        self.right = Node()
        self.left.next = self.right
        self.right.prev = self.left

    # 把节点从链表中拆下来
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # 放到最右边，表示最近使用
    def _add(self, node):
        last = self.right.prev

        last.next = node
        node.prev = last
        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # 移到最右边
        self._remove(node)
        self._add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
        else:
            node = Node(key, value)
            self.cache[key] = node

        self._add(node)

        # 超容量，淘汰最久没使用的节点
        if len(self.cache) > self.capacity:
            oldest = self.left.next
            self._remove(oldest)
            del self.cache[oldest.key]
        
