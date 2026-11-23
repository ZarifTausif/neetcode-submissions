class Solution:
    def longestConsecutive(self, nums: List[int]) ->int:
        if not nums:
            return 0
        seen=sorted(set(nums))
        series=1
        longest=1
        for i in range(1,len(seen)):
            if seen[i]==seen[i-1]+1:
                series+=1
            else:
                series=1
            if series>longest:
                longest=series
        return longest
