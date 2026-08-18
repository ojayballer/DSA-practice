class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash =defaultdict(int)
        for i in nums :
            hash[i]+=1
        res=[]
        while k>0 :
            top=max(hash,key=hash.get)
            res.append(top)
            hash.pop(top)
            k-=1
        return res 
            

