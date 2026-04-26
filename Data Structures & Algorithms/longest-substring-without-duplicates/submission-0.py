class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       char= set() ; l=0 ;res=0
       for r in range(len(s)):
           while s[r] in char :
               char.remove(s[l])
               l+=1
           char.add(s[r])
           res=max(res,r-l+1)
       return res 


       #==============test case=======
       #pwwkew 
       # p is not in char ,so add p to char,res becomes (0,0-0+1)=1,p
       #w is not present,so add it to char,res becomes (1,1-0+1)=2,pw
       #w is in char already ,so pop p(l=1) then while loop pops w(l=2) again starts a new sequence, set={},then add w back to set,res
       # becomes (2,2-2+1)=2
       #k is not in so add k to set,set={w,k},res=(2,3-2+1)=2
       # same for e ,add e to set,set ={w,k,e} ,res=(2,4-2+1)=3
       # w is in set ,so pop w , then increase l,if w is still in set keep popping the char[l](lbecomes 3),since w is not in set again,we add w to set ,set={k,e,w} ,
       #then res wouuld be res=res(3,3-3+1)==3 ,3 is the length of the longest substring !
