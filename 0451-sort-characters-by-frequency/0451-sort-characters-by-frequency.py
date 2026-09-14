class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        for ch in s:
            freq[ch]=1+freq.get(ch,0)
        
        res=""
        for ch in sorted(freq,key=freq.get,reverse=True):
            res+=ch*freq[ch]
        return res        