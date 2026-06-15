class MyHashMap:

    def __init__(self):
        self.dict1 ={}
        

    def put(self, key: int, value: int) -> None:
        self.dict1[key] = value

    def get(self, key: int) -> int:
        if key in self.dict1.keys():
            return self.dict1[key]
        return -1
        

    def remove(self, key: int) -> None:
        if key in self.dict1.keys():
            self.dict1.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)