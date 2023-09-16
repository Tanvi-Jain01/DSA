class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x_str=str(x)

        reversee=x_str[::-1]
        print(reversee)
        
        if reversee==str(x):
            return True
        else:
            return False
        