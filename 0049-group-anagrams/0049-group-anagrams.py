class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for n in strs:
            key="".join(sorted(n))
            if key in freq:
                freq[key].append(n)
            else:
                freq[key]=[n]
        return list(freq.values())
        