class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
                nums1.append(i)
        nums1.sort()        
                
        N = len(nums1)
        if N%2!=0:
            return nums1[(N)//2]
        else:
            return (nums1[N//2-1] + nums1[N//2])/2