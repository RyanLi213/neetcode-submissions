class Solution:
    def isPalindrome(self, s: str) -> bool:
        d= []
        for i in s:
            if i.isalnum():
                d.append(i)
        
        d = [str(var).lower().strip() for var in d]

        for i in range(len(d)):
            if d[i] != d[::-1][i]:
                return False
        return True
        
        