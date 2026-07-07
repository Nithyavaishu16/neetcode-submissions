class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ''
        for s in strs:
            encodedString += str(len(s)) + '%' + s
        
        return encodedString

    def decode(self, s: str) -> List[str]:
        res = []
        idx = 0
        while idx < len(s):
            startingIdx = idx
            # extract length of string by iterating through the digits until we hit the %
            while s[idx].isdigit():
                idx += 1
            
            # something went wrong
            if s[idx] != '%':
                break
            
            lenString = int(s[startingIdx : idx])
            res.append(s[idx + 1 : idx + lenString + 1])
            idx += 1 + lenString

        return res

            


