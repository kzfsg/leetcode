# LRU Cache -> able to keep track of the least recently used item
# get must be O(1) -> Hashmap?
# we need O(1) insertion / deletion of the least recently used, so we use doubly linked list
class LRUCache(object):

    class Node:
        def __init__(self, key=0, value=0):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}

        self.head = self.Node()
        self.tail = self.Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # this helper removes node from current position
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):
        # helper adds a node after the head
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_to_head(node)
        return node.value
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self._remove(self.cache[key])

        new_node = self.Node(key, value)
        self.cache[key] = new_node
        self._add_to_head(new_node)

        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)