# Check palindrome ex_138p
# 125. Valid Palindrome
# alphanumeric problem
# https://leetcode.com/problems/valid-palindrome/
# 'A man, a plan, a canal: Panama'
class Solution:
    # input must be String type, return must be boolean type
    def isPalindrome(self, s:str) -> bool:
        # make list
        strs = []
        for char in s:
            # islnum(letter&number), isahlpa(alphabet), isdigit(number)
            if char.isalnum():
                strs.append(char.lower())
            # ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c',
            #  'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']

        # Until left one char
        while len(str)>1:
            # pop 1st String => pop(0), pop last String => pop()
            if strs.pop(0) != strs.pop():
                return False

        return True

