class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for ch in nums:
            if ch in seen:
                return True
            seen.add(ch)
        return False
        