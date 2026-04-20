class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        print(output)
        
        return output


    def decode(self, s: str) -> List[str]:
        res = []

        j = 0
        i = 0
        while i < len(s):
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j + 1 + length
            j = j + 1 + length
        
        return res

