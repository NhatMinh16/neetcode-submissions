class MyHashMap:

    def __init__(self):
        self.size = 10
        self.data = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return key % 10

    def put(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        bucket = self.data[index]
        for i, [k, v] in enumerate(bucket):
            if k == key:
                bucket[i] = [key, value]
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        bucket = self.data[index]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = self.hash_function(key)
        bucket = self.data[index]
        for i, [k, v] in enumerate(bucket):
            if k == key:
                del bucket[i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)