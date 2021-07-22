#hash table with collision handling by chaining. In chaining for multiple elements to be stored at same index , the key along with the data is stored at that location


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for i in key:
            hash+= ord(i)
        return hash % self.MAX

    def getvalue(self,key):
        arr_index = self.get_hash(key)
        for i in self.arr[arr_index]:
            if i[0] ==  key:
                return  i[1]

    def setvalue(self,key,value):
        h = self.get_hash(key)
        for idx,ele in enumerate(self.arr[h]):
            if len(ele) == 2 and ele[0] == key:
                self.arr[h][idx] = (key,value)
            else:
                self.arr[h].append((key,value))

    def delitem(self,key):
        temp = self.get_hash(key)
        for idx,kv in enumerate(self.arr[temp]):
            if kv[0] == key:
                self.arr[temp][idx] = None

if __name__ == '__main__':
    h = HashTable()
    h.setvalue('march 6',25)
    h.setvalue('march 9',26)
    h.setvalue('march 17',150)
    print(h.arr)
