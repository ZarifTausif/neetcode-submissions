class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip().lower()
        string=''
        for c in s:
            if c.isalnum():
                string+=c
        return string==string[::-1]