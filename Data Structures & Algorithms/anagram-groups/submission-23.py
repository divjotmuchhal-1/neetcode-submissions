class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for s in strs:
            charArray = [0] * 26

            for c in s:
                charArray[ord(c) - ord('a')] += 1
            
            myDict[tuple(charArray)].append(s)
        
        return list(myDict.values())

        