class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i - 1]
        return nums
    
    
    #  time complexity - O(N)
    # space complexity - O(1)