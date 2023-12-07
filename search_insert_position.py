class Solution:
    #given a sorted array of distinct int and target val, return index if target is found
    #if not return indec where it would be if it were inserted in order.
    def searchInsert(self, nums: list[int], target: int) -> int:
        #log(n)
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = (1 + r) // 2

            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return 1