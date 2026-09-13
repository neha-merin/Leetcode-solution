class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen=set()
        res=set()
        for ch in nums1:
            if ch in seen:
                continue
            seen.add(ch)
        for ch in nums2:
            if ch in seen:
                res.add(ch)
        return list(res)

        