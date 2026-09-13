class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=set()
        for ch in nums1:
            for ch1 in nums2:
                if ch==ch1:
                    res.add(ch)
        return list(res)
        