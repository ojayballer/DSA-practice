class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for str in strs :
            Sorted = ''.join(sorted(str))  # if similar keys are sorted ,they form the string order eventually and then
            # we can use the sorted order  to append a string  to the right group
            # also default dict would never return an error for a key that doesnt exist yet ,instead it creates the key
            hashmap[Sorted].append(str)

        return list(hashmap.values())


