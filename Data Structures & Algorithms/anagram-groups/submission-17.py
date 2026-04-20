class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)

        for s in strs:
            strArr = [0 for _ in range(26)]
            for c in s:
                strArr[ord(c) - ord('a')] += 1
            
            myDict[tuple(strArr)].append(s)
        

        return list(myDict.values())
