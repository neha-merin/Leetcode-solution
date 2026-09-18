class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map={0:-1}
        rsum=0
        maxi=0
        for i in range(len(nums)):
            if nums[i]==0:
                rsum-=1
            else:
                rsum+=1
            if rsum in map:
                length=i-map[rsum]
                maxi=max(length,maxi)
            else:
                map[rsum]=i
        return maxi
        