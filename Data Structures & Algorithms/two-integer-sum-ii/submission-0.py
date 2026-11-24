class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            compliment=target-numbers[i]
            l,r=i+1,len(numbers)-1
            while l<=r:
                m=l+(r-l)//2
                
                if numbers[m]==compliment:
                    return [i+1,m+1]
                elif numbers[m]<=compliment:
                    l=m+1
                else:
                    r=m-1
        return []