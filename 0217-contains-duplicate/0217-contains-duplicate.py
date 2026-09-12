class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for ch in nums:
            freq[ch]=1+freq.get(ch,0)
        for ch in nums:
            if freq[ch]>1:
                return True
                break
        return False
        