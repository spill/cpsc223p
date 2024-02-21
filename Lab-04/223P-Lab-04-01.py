def is_palindrome(s):
    str = s.lower()
    stack = []
    
    for characters in str:
        stack.append(characters)
        
        
    for characters in str:
        if characters != stack.pop():
            return False
    
    return True

# Test the function
print(is_palindrome("lol"))  # This will return true