class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps={}
        for w in strs:
            arr= [0]*26
            for c in w:
                arr[ord(c)-ord('a')]+=1
            arr=tuple(arr)
            if arr in grps:
                grps[arr].append(w)
            else:
                grps[arr]=[w]
        return [grps[k] for k in grps]