class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        f1=Counter(nums1)
        f2=Counter(nums2)
        ans=f1 & f2
        return list(ans.elements())