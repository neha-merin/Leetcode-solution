class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq={}
        seen=set()
        for ch in arr:
            freq[ch]=1+freq.get(ch,0)
        for ch in freq:
            if freq[ch] in seen:
                return False
            seen.add(freq[ch])
        return True