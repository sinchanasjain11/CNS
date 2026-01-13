import re 
def check_password_strength(password):
    if len(password)<8:
        return "weak:password should be at least 8 characters."
    if not re.search("[a-z]",password):
        return "weak:password should have at least one lowercase letter "
    if not re.search("[A-Z]",password):
        return "weak:password should have at least one uppercase letter "
    if not re.search("[0-9]",password):
        return "weak:password should have at least one digit "
    if not re.search("[!@#$%^&*()<>?:{}?|<>]",password):
        return "weak :password should have at least one special character"
    return "strong password!"
password=input("enter a password")
print (check_password_strength(password))       
