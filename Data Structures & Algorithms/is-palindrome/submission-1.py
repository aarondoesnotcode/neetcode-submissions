class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = s.lower()
        string = ""

        for i in range(len(str)):
            if str[i].isalnum():
                string += str[i]

        l = 0
        r = len(string) - 1

        print(string)

        while l < r:
            if string[l] != string[r]:
                return False
            l += 1
            r -= 1
        
        return True



        