class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total=sum(nums)
        target=total%p
        if target==0:
            return 0
        prefix=0
        freq={0:-1}
        ans=len(nums)
        length=0
        for i in range(len(nums)):
            prefix+=nums[i]
            rem=prefix%p
            need=(rem-target)%p
            if need in freq:
                length=i-freq[need]
                ans=min(ans,length)
            freq[rem]=i
        if ans==len(nums):
            return -1
        else:
            return ans

        