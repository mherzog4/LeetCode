class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_val = 0
        total = 0
        
        for num in nums:
            total += num
            min_val = min(min_val, total)
            
        return -min_val + 1
    
#     Time complexity: O(N) - in this method we just traverse the array once

# Space complexity: O(1) - we need to calculate the step-by-step total of the arrya and record the min step by step total, both only require constant space