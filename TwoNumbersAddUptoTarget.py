
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dir = {}
        for i, n in enumerate(nums):
            if target - n in dir:
                return [dir[target - n], i]

            dir[n] = i