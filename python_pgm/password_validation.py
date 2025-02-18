import re
def is_valid_password(string:str):
    if len(string)  < 8 and len(string) > 16:
        print("length of is ❎")
    else:
        print("length of is ✅ ") 
        
    if not re.search(r'[A-Z]', string):
        print("Upper Case of is ❎")
    else:
        print("Upper Case of is ✅ ") 
        
    if not re.search(r'[a-z]',string):
        print('lower Case is ❎')
    else:
        print("lower Case of is ✅ ") 
         
    if not re.search(r'[0-9]',string):
        print('Digit is ❎')
    else:
        print("Digit of is ✅ ") 
        
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]',string):
        print('Special Charter is ❎')
    else:
        print("Special Charter is ✅ ") 
        
    common_passwords = ['password123', '123456', 'qwerty', 'abcdef', 'password']
    if string.lower() in common_passwords:
        print('Password is too common')
        
    if re.search(r'(.)\1{2,}', string):  # Repeating characters
        print( "Password cannot have repeating characters.")
    if re.search(r'(012|123|234|345|456|567|678|789)', string):  # Sequential digits
        print("Password cannot have sequential digits.")
        
    print("Password is Valid ✅")
        
        
def validate_password(password:str):
    if len(password) < 8 or len(password) > 20:
        print("length of is ❎")
    else:
        print("length of is ✅ ") 
        
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
            # print("Upper Case of is ✅ ") 
        elif char.islower():
            has_lower = True
            # print('lower Case is ❎')
        elif  char.isdigit():
            has_digit = True
            # print("Digit of is ✅ ") 
        elif char in "!@#$%^&*(),.?\":{}|<>":
            has_special = True
            # print("Special Charter is ✅ ") 
            
    common_passwords = ['password123', '123456', 'qwerty', 'abcdef', 'password']
    if password.lower() in common_passwords:
        print('Password is too common') 
        
    
    for i in range(len(password) - 2) :
        if password[i] == password[i + 1] == password[ i+2]:
            print('Password cannot have repeating character')
        
        if password[i:i+3].isdigit():
            if int(password[i+1]) == int(password[i])+1 and int(password[i + 2]) == int(password[i]) +2:
                print('Password cannot have sequential digits')
    
    print("Password is valid")
        
        
password = "Password123!"
validate_password(password)