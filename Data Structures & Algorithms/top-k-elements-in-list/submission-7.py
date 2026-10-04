class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # hashmap to tracj te current most freuwnt elemnt 
       # and then return k most frequent  elements 
       # hm to store the count and key of eeach elemt 
       #return the key's with the most k counts 

       hm= defaultdict(int)
       for i in range(len(nums)):
         hm[nums[i]]+=1
       res=[]
       while k >0 :
         res.append(max(hm,key=hm.get))
         del hm[max(hm,key=hm.get)]
         k-=1 
       return res 

