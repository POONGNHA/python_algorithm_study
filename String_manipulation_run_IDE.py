def isPalindrome(s = 'A man, a plan, a canal: Panama'):
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # Until left one char
    while len(strs)>1:
        # pop 1st String => pop(0), pop last String => pop()
        if strs.pop(0) != strs.pop():
            return False
    return True
print(isPalindrome())

