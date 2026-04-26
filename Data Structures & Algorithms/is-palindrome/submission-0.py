class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s=''
        for c in s:
            if c.isalnum() ==True:
                clean_s+=c.lower()
        return clean_s== clean_s[::-1]


