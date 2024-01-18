## Using Freq table
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        m = {}
        for i in arr:
            if m.get(i):
                m[i]+=1
            else: m[i] = 1
                
        for i in arr:
            if m[i] == 1 : k-=1
            if k ==0 : return i
            
        return ""
            
        
## using list comprehension
    
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a = [i for i in arr if arr.count(i)==1]
        return "" if k>len(a) else a[k-1]
        
        