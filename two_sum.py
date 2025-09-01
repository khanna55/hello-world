#1. Two Sum Problem
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_map = {}
      for i in range(len(nums)):
        if target - nums[i] in hash_map:
          return [hash_map[target-nums[i]], i]
        hash_map[nums[i]] = i
sol = Solution()
sol.twoSum([2,7,11,15], 9)
            
