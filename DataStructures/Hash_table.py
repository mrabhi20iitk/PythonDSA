class Hash_table:
    def __init__(self):
        self.MAX = 100
        self.arr = [[None] for i in range(100)]

    def get_hash(self,key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % self.MAX

    #calling a value
    def getitem(self, item):
        h = self.get_hash(item)
        return self.arr[h]

    #assigning an value
    def setitem(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
        return self.arr[h]

    #deleting an value
    def delitem(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        return self.arr[h]

if __name__ == '__main__':
    h = Hash_table()
    h.setitem('march 26',"Abhishek's birthday")
    h.setitem('mar 25',"My sister's birthday")
    print(h.getitem('april 25'))
    print(h.arr)
    h.delitem('april 25')
    print(h.arr)
