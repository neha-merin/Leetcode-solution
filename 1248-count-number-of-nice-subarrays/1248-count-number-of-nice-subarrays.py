class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        freq={0:1}
        prefix=0
        count=0
        for i in range(len(nums)):
            if nums[i]%2==1:
                prefix+=1
            else:
                prefix+=0
            diff=prefix-k
            if diff in freq:
                count+=freq[diff]
            freq[prefix]=1+freq.get(prefix,0)
        return count
            

        