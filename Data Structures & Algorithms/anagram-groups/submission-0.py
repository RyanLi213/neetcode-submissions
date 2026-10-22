class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dictionary = defaultdict(list)
        for string in strs:
            count = [0]*26
            for s in string:
                count[ord(s)-ord("a")]+=1
            
            key = tuple(count)
            dictionary[key].append(string)
        
        return list(dictionary.values())