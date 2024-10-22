# two sum
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #Dictionary to store value and its index
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            # If complement does not exist, store the current number with its index
            num_dict[num] = i

sol = Solution()

# Test case
nums = [2, 7, 11, 15]
target = 9
result = sol.twoSum(nums, target)

# Output the result
print(result)