class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # f1=Counter(nums1)
        # f2=Counter(nums2)
        # ans=f1 & f2
        # return list(ans.elements())

        f1=dict(Counter(nums1))
        ans=[]
        for n in nums2:
            if(n not in f1 or f1.get(n)==0):
                continue
            else:
                ans.append(n)
                f1[n]-=1
        return ans