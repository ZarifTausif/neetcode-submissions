class Solution:
    def longestConsecutive(self, nums: List[int]) ->int:
        seen=set()
        for n in nums:
            seen.add(n)
        seen=list(seen)
        seen.sort()
        series=1
        longest=0
        for i in range(len(seen)):
            if (seen[i]==seen[i-1]+1):
                series+=1
                if i!=len(seen)-1:
                    continue
            if series>longest:
                longest=series
            series=1
        return longest
