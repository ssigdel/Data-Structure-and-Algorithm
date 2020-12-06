class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    
    #takes key and return the hash value
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
    
    #takes key and value as input and inserts into hashtable
    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

#driver function
if __name__ == "__main__":
    hash = HashTable()
    hash.add("dec 12", 120)
    print(hash.arr)