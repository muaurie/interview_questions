#using the heights, whats the biggest area we can form with a container that has a left height and a right height.
class Solution:
    def maxArea(self, height: list[int]) -> int:
        #brute force
        res = 0
        #slow
        for l in range(len(height)):
            for r in range(l+1, len(height)):
                #compute
                area = (r - l) * min(height[l]), min(height[r])
                #update res after ea. calc
                res = max(res, area)
            return res
        #linear time solution: O(n)
    def maxArea1(self, height: list[int]) -> int:
        #two pointer technique
        res = 0
        l, r =  0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l]), min(height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res

