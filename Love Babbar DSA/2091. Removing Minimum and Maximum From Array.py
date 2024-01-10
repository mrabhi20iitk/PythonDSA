class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        max_num = max(nums)
        min_num = min(nums)
        a, b = 0,0
        for i in range(len(nums)):
            if nums[i] == max_num : a = i
            if nums[i] == min_num : b = i
                
        x = min(a,b)
        y = max(a,b)

                
        n = len(nums)        
        return min(x+n-y+1, y+1 , n-x)
        