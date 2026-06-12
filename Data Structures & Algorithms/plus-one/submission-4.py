class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if not digits :
            return [1]
        
        if digits[-1] < 9: # if digits less than 9 ,just add one to the last digit
            digits[-1]+=1
            return digits 

        return self.plusOne(digits[:-1]) +[0] # if digit is 9,recurse on evry digit except the last and add 0 to the end