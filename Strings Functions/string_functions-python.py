#string defs project
def revers(str):
    # Accept an input string, str, and reverse its characters in order
    s=str[::-1]
    return s

def uppercase(str):
    # Convert all the characters of the input string, str, to upper
    # case. Reurn the uppercased string.
    s=str.upper()
    return s
def palindrome(str):
    # Check if the input string, str, is spelled the same forwards
    # as it is spelled backwards.
    # Return "is a palindrome" if it is, or "is not a palindrome" if it is not.
    if (str==revers(str)):
        return "is a palindrome"
    else :
        return "is not a palindrome"