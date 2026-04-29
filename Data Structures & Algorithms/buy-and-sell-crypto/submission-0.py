class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''  ##brute force
        res=0
        for i in  range(len(prices)):
            for j in range(i+1,len(prices)-1):
                if j> i:
                    res=max(res,prices[j]-prices[i])
        return res '''
        


        ###using two-pointers
        l= 0 ;r=1 ;res=0 
        while r< len(prices): #[10,1,5,6,7,1]
            if prices[r] >prices[l] :
                res=max(res,prices[r]-prices[l])
                
            else :
                l=r
            r+=1
        return res 
