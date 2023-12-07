#Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
#The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l, r = 0, 0

        while r < len(nums):
            count = 1
            while r + 1 < len(nums) and nums[r] == nums[r+1]:
                r += 1
                count += 1
            for i in range(min(2, count)):
                nums[1] = nums[r]
                l += 1
            r += 1
        return