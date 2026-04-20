class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        charDict = defaultdict(list)
        for string in strs:
            charArr = [0] * 26
            for c in string:
                charArr[ord(c) - ord('a')] += 1
            charDict[tuple(charArr)].append(string)
        return (list(charDict.values()))

        