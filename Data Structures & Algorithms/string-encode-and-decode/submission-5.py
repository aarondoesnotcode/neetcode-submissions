class Solution:

#encode sol, use the len for the integer, # for delimiter
    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + '#' + s
        return string

#string - 4#neet
    def decode(self, s: str) -> List[str]:
        res = []
        #we are going to use this to read through the words
        i = 0

        while i < len(s):
            #using j to find the end of the int
            j = i
            while s[j] != '#':
                j += 1
                    #remember, it might be a double digit length etc
            n = int(s[i:j])
            res.append(s[j+1:j + 1 + n])
            i = j + 1 + n


        return res


