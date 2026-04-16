class Solution:

    def encode(self, strs: List[str]) -> str:
        #encode it in a form of number 3#test
        newStr = ""
        for string in strs:
            newStr += str(len(string)) + "#" + string
        return newStr


    def decode(self, s: str) -> List[str]:
        #need to decode string 4#test6#blabla -> [test, blabla]
        strs = []
        count = 0

        while count < len(s):
            num = ""
            while s[count]!= "#":
                num += s[count]
                count += 1
            strs.append(s[count + 1: count + 1 + int(num)])
            count = count + 1 + int(num)
        #the reason i was getting empty string errors, was because the count
        #wasn't going back to the next digit properly, due to line 22
        #prev: count + 2 + int(num)...
        #silly mistake, it was cause of my example, '3#test...' its obvs '4#test'

        return strs
                
                    


        