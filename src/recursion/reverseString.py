def rev (theString: str) -> str:
    if len(theString) == 0 or len(theString) == 1:
        return theString
    
    head, tail = theString[0], theString[1:]
    return rev(tail) + head

print(rev("Hello World!"))  # Output: "!dlroW olleH"

print(rev("Python"))  # Output: "nohtyP"

print(rev("12345"))  # Output: "54321"

print(rev(""))  # Output: ""

print(rev("a"))  # Output: "a"

print(rev("ab"))  # Output: "ba"

print(rev("abc"))  # Output: "cba"