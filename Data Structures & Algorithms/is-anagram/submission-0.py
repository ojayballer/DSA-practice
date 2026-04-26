class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        '''
     s.sorted()
     t.sorted()
     for i in range(len(s)):
        for j in range(len(t)):
            if s[i]== t[j] :
               return True
     else :
        return False  
        '''