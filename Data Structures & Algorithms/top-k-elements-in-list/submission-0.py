class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count={}
      for num in nums:
        ## if num doesn't exist in count,createthe key,return 0 and add 1,but if it does return the previous count and add 1
        #it only  create a new key if there is a new unique elemnt 
        count[num]=count.get(num,0) +1 
      
      arr=[]
      for num,freq in count.items():   #[[key,value],..]
        arr.append([freq,num])  # add elemnts to array in l[freq,num]
      arr.sort() # sort by increasing order of freq by defaut,no key needed 

      res=[] # store results
      while len(res) < k: #while the len(res) is less than k,basically these 
        res.append(arr.pop()[1]) #pop the first tuple and append the result to res 
      #keep popping until we reach  the top k -elemnts we want 
      
      res.sort()
      return res


##test case
#[1,2,2,3,3,3] ,k=2
# 1 is not in hashmap ,so we create num[0] which retrns 0 +1=1 ,hm={0;1}
#2 is not in hahsmap,so it becomes ,hm={1;1,2;1},basically we add 2 to the hashmap and update it's count to 1
#2 is in hahsmap  already ,the cureent count is 1 ,we use .get() to return it so it becomes ,hm={0;1,1;2}
#3 is not in hashmap,count becomes 1,hm={{1;1,2;2,3;1}
#3 is in hashmpa,count becomes 2,hm={1;1,2;2,,3;2}
#3 is in hashmpa,count becomes 3,hm=1;1,2;2,,3;3}

# we loop through each number and freuency ,and create a new list in the form [freq,num]  so we can sort by frequency:
# array becomes =[[1,1],[2,2],[3,3]]

# now  we want to return te top k most frequent elements ,so we can keep removing the last element( .pop()[1] grabs the number instead of frequency) and storing it ,until we have the k 
#elemnts we want,so if len(res)< k-lemnts ,keep popping the  elemnt and storing it in result,
#and then we would return result !
#since k=2
#len(res) which is equal to 0 is less than k,then res becomes:
#res=[3,2] ,now the problem statement did not say we should return the results in ascending order ,but i wanna do that to be safe,so
# i am going to do  res.sort() to sort the numbers 


                

        