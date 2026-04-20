class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)

        for s in strs:
            myList = [0] * 26

            for c in s:
                myList[ord(c) - ord('a')] += 1
            myDict[tuple(myList)].append(s)
        
        return myDict.values()
        