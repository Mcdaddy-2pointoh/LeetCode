
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        tots = nums1 + nums2
        tots.sort()
        size = len(tots)
        ind = size / 2

        if size % 2 == 0:
            return (tots[ind] + tots[ind-1])/2

        else:
            return tots[ind]
