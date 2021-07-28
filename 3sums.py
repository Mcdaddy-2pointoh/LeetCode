class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        nums.sort()
        res = []
        n = len(nums)

        for num in range(n-2):
            if num > 0 and nums[num] == nums[num-1]:
                continue
            left = num + 1
            right = n - 1
            while left < right:

                total = nums[num] + nums[left] + nums[right]
                if (left > num+1 and nums[left] == nums[left-1]) or total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                elif total == 0:
                    res.append([nums[num], nums[left], nums[right]])
                    left += 1

        return res