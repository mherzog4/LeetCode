class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            curr = target - nums[i]
            if curr in hash:
                return [i, hash[curr]]
            hash[nums[i]] = i
                