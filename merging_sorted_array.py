class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        #no returns modify nums1 in place
        #del nums1[m:]
        #nums1.extend(nums2)
        #nums1.sort()
        i,j,k= 0,0,0
        temp = nums1.copy()
        while i<m and j<n:
            if temp[i] < nums2[j]:
                nums1[k] = temp[i]
                i+=1
            else:
                nums1[k] = nums2[j]
                j+=1
            k+=1
        while i<m:
            nums1[k] = temp[i]
            i+=1
            k+=1
        while j<n:
            nums1[k] - nums2[j]
            j+=1
            k+=1