class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)

        for s in strs:
            ordArr = [0] * 26
            for c in s:
                ordArr[ord(c) - ord('a')] += 1
            
            myDict[tuple(ordArr)].append(s)
        

        return list(myDict.values())
