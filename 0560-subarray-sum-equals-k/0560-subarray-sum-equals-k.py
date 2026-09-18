class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq={0:1}
        count=0
        prefix=0
        for n in nums:
            prefix+=n
            diff= prefix-k
            if diff in freq:
                count+=freq[diff]
            freq[prefix]=1+freq.get(prefix,0)
        return count
        
        