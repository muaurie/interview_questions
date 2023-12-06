class Solution:
#given an array of strings (nums) containing n unique binary strings of ea. len n, return a binary string of length n that does not appear in nums.
#if multiple answers, return any of them
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        #backtrack approach
        #generate a bunch of binary strings until we get the right one
        strSet = { s for s in nums }
        def backtrack(i, cur):
            if i  == len(nums):
                    #is this str in cur = to one str in set
                    #join str in cur to be a str
                res = "".join(cur)
                #return null if this result is in str set bc we want to return something that ISNT in the set
                return None if res in strSet else res
            #first decision
            #i + 1 to shift to the next position ea. time
            res = backtrack(i + 1, cur)
            #if result not null, return to not generate extra str
            if res: return res
            #2nd decision: change decision to be 1 at index.
            cur[i] = "1"
            res = backtrack(i + 1, cur)
            #if result not null, return to not generate extra str
            if res: return res

                
        #call func
        return backtrack(0,["0" for s in nums])
