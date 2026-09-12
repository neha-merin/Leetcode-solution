class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        for ch in nums:
            ans.append(ch)
        for ch in nums:
            ans.append(ch)
        return ans