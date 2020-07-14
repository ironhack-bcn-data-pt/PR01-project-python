import random as rd

digit1=["abcdefghijklmnopqrstuvwxyz","0123456789","ABCDEFGHIJKLMNOPQRSTUVWXYZ","@#%$&*-_"]

def f_usuario():
    user=input("Please intruduce your user name ")
    
    return user

def f_len():
    print("Please choose the length of your password")
    number_len =int(0)
    while number_len < 4 or number_len > 12:     
        try:
            number_len = int(input("Password length? "))
        except ValueError:
            print("You can not choose a string")
        
    return int(number_len)

lenght = f_len()

def f_password():
    password= ""
    for c in range(lenght):
        password +=rd.choice(digit1[c%len(digit1)])
    password=list(password)
    rd.shuffle(password)
    password1= ""
            
    return password1.join(password)

password=f_password()

password

def main():
    print("Welcome to your password generator")
    print("Your password will be generated with upper and lower letters, special characters and numbers")
    print("You can choose the length of your password between 4 and 12 characters")
    print(" ")
    usuario= f_usuario()
    
    print(f"Confirmation for the user : {usuario}, the password is generated : {password}")
    return 
main()