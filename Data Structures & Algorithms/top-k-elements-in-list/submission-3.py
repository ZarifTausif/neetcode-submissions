class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        freq={}
        for n in nums:
            if n not in freq:
                freq[n]=0
            freq[n]+=1
        i=0
        while i!=k:
            maxcount=0
            maxnum=0
            for key in freq:
                if freq[key]>maxcount:
                    maxcount=freq[key]
                    maxnum=key
            res.append(maxnum)
            del freq[maxnum]
            i+=1
        return res
            