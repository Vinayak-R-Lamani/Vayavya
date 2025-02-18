def is_Palindrome(string:str):
    return string == string[::-1]

s = "madam"
print("Palindrome"  if is_Palindrome(s) else "Not a Palindrome")

    