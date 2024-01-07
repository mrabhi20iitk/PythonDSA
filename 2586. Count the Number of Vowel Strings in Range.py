class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        def ifvowel(w):
            if w=='a'or  w== 'e' or w=='i' or w=='o' or w=='u':
                return True            
            return False
        
        count = 0
        for i in range(left,right+1):
            if ifvowel(words[i][0]) == ifvowel(words[i][-1]) == True:
                count+=1
        return count