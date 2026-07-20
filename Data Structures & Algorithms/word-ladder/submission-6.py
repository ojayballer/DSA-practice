class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
      if endWord not in wordList  or endWord==beginWord:
        return 0
      beginQ=collections.deque([beginWord])
      endQ=collections.deque([endWord])

      visitBegin=set()
      visitBegin.add(beginWord)
       
      visitEnd=set()
      visitEnd.add(endWord)

      StepsBegin=1 
      StepsEnd =1 

      wordSet=set(wordList) # O(1) look-up
      

      res=0
      while beginQ and endQ :
          if len(beginQ)>len(endQ):
            beginQ,endQ=endQ,beginQ
            visitBegin,visitEnd=visitEnd,visitBegin 
            StepsBegin,StepsEnd=StepsEnd,StepsBegin

          for j in range(len(beginQ)):
            word=beginQ.popleft()
            for index in range(len(word)):
              for c in 'abcdefghijklmnopqrstuvwxyz':
                  nei= word[:index] + c +word[index+1:]
                  if nei in visitEnd :
                    return StepsBegin+StepsEnd
                  if nei in wordSet and nei not in visitBegin :
                      beginQ.append(nei)
                      visitBegin.add(nei)
          
          StepsBegin+=1
      return 0
      
      

          

                 


