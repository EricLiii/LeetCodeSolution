class LRUCache:

#Wrong solution

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.map = {}
        self.dic = {}
        
    def get(self, key: int) -> int:
        if key in self.dic:
            k = self.queue.pop(self.map[key])
            self.queue.append(k)
            self.map[k] = len(self.queue)-1
            return self.dic[key]
        else: return -1

    def put(self, key: int, value: int) -> None:
        if len(self.dic) >= self.capacity:
            k = self.queue.pop(0)
            self.dic.pop(k)
            self.map.pop(k)
        if key in self.queue:
            self.queue.pop(self.map[key])

        self.queue.append(key)
        self.dic[key] = value
        self.map[key] = len(self.queue)-1