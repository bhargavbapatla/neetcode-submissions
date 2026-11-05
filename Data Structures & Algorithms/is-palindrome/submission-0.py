class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''
        for i in s:
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 48 and ord(i) <= 57):
                res+=i.lower()
        return res == res[::-1]
