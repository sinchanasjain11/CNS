def is_password_commonly(password:str,common_password:list)->bool:
    return password in common_password
common_passwords=['123456','password','123456789','qwerty','abc123']
password='viggachu'
if is_password_commonly(password,common_passwords):
    print("password is too common!")
else:
    print("password is not common.")
    