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