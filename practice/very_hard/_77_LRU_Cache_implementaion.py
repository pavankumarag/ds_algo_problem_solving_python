import collections

class LRUCache2: # using ordered dict
    def __init__(self, capacity):
        self._dict = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self._dict:
            self._dict.move_to_end(key)
            return self._dict[key]
        return -1

    def put(self, key, value):
        self._dict[key] = value
        self._dict.move_to_end(key)

        if len(self._dict) > self.capacity:  # Time to evict the oldest
            self._dict.popitem(last=False)

class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.cache = {}
		self.queue = DoubleEndedDoublyLL()


	def get(self, key):
		if key in self.cache:
			node = self.cache[key]
			self._advance(node)
			return node.val
		else:
			return -1


	def put(self, key, value):
		if key in self.cache:
			node = self.cache[key]
			node.val = value
			self._advance(node)
		else:
			if len(self.queue) == self.capacity:
				last_item = self.queue.pop()
				del (self.cache[last_item.key])

			node = DoublyLinkedNode(key, value)
			self.queue.appendleft(node)
			self.cache[key] = node


	def _advance(self, node):
		self.queue.remove(node)
		self.queue.appendleft(node)


class DoubleEndedDoublyLL:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __len__(self):
		return self.size

	def appendleft(self, node):
		if not self.head:
			self.head = node
			self.tail = node
		else:
			prev_head = self.head
			node.next = prev_head
			self.head = node
			prev_head.prev = node

		self.size += 1

	def pop(self):
		tmp = self.tail
		self.remove(self.tail)
		return tmp

	def remove(self, node):
		prev_node = node.prev
		next_node = node.next

		if self.tail == node:
			self.tail = prev_node
		if self.head == node:
			self.head = next_node

		if prev_node:
			prev_node.next = next_node

		if next_node:
			next_node.prev = prev_node
			node.prev = None

		self.size -= 1


class DoublyLinkedNode:
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.prev = None
		self.next = None


if __name__ == "__main__":
	cache = LRUCache(2)
	cache.put(1, 1)
	cache.put(2, 2)
	print cache.get(1) # returns 1
	print cache.put(3, 3) # evicts key 2
	print cache.get(2) # returns - 1(not found)
	print cache.put(4, 4) # evict key 1
	print cache.get(1) # returns - 1(not found)
	print cache.get(3) # returns 3
	print cache.get(4) # returns 4

