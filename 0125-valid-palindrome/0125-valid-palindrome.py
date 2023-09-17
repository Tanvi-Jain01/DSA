class Solution:
    def isPalindrome(self, s: str) -> bool:
        c=s.lower()
        real=''
        for i in c:
            if i.isalnum():
                real+=i

        reversee=real[::-1]
        if reversee==real:
            return True
        else:
            return False


        