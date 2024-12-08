def check_password(password):
    is_strong_pwd = []

    # check length of password
    if len(password) > 8:
        is_strong_pwd.append(True)
    else:
        is_strong_pwd.append(False)

    # Check at least 1 upper letter
    for i in password:
        if i.isupper():
            is_strong_pwd.append(True)
            break
    # Check number
    for j in password:
        if j.isdigit():
            is_strong_pwd.append(True)
            break
    if all(is_strong_pwd):
        return "Strong password"
    else:
        return "Weak password"


password = input("Enter your password: ")
print(check_password(password))



