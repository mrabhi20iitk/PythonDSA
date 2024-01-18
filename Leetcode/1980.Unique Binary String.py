
#Cantor's Diagonal Argument -- traversing diagonally and using opposite of the string 

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            ans.append("1" if nums[i][i]=='0' else '0')
        
        return "".join(ans)
