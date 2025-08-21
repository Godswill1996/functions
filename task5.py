#TASK5
'''
Write a function called check_password_strength that takes a password string and returns "weak","medium", or "strong" based on t
these citeria: weak(less than 6 characters),medium(6-10 characters),strong(more than 10 characters and contains both letters and numbers).
'''

def check_password():
    password = input("Enter password:")
    for i in password :
        if len(password) >= 0 and len(password) <6 :
            print(f"Password {password} is weak")
            break
        elif len(password) >=6 and len(password) <= 10 :
            print(f"password {password} is medium")
            break
        elif len(password) > 10 :
            print(f"password {password} is strong")
            break
check_password()
