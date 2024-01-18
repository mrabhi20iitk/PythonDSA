#Solution 1 : List comprehension :
```
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum([1 for i in words if s[:len(i)] == i])
        
```


#Solution  2  : Using dictionary
```
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        m = {}
        for i in range(len(s)):
            m[s[0:i+1]] = 1
         
        count = 0
        for i in words:
            if m.get(i):
                count+=1
            else:
                continue
        
        return count
        
```

#Solution 3 : For loop with list slicing:
```
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for i in words:
            if (s[:len(i)]) == i:
                count+=1
                
        return count
```

