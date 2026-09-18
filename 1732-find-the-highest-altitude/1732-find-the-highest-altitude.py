class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt=0
        highest=0
        for g in gain:
            highest+=g
            alt=max(alt,highest)
        return alt
        