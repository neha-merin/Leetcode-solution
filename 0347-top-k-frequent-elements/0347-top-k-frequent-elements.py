class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for n in nums:
            freq[n]=1+freq.get(n,0)
        return sorted(freq, key=freq.get, reverse=True)[:k]