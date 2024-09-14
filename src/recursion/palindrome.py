def isPalindrome(theString: str) -> bool:
    if len(theString) <= 1:
        return True
    
    firstChar = theString[0]
    middleChars = theString[1:-1]
    lastChar = theString[-1]
    
    return firstChar == lastChar and isPalindrome(middleChars)

print(isPalindrome("racecar"))  # True

print(isPalindrome("hello"))  # False

print(isPalindrome("a"))  # True

print(isPalindrome(""))  # True

print(isPalindrome("12321"))  # True

print(isPalindrome("12345"))  # False

print(isPalindrome("!@#$%^&*()"))  # False

print(isPalindrome("radar"))  # True

print(isPalindrome("hello, world!"))  # False