import random
import string

# password variables:
# - length
# - uppercase flag
# - digits flag
# - special char flag

def generate_password(password_length, upper_flag, digits_flag, special_flag):

    # lowercase alphabet
    characters = string.ascii_lowercase

    if upper_flag:
        characters += string.ascii_uppercase
    if digits_flag:
        characters += string.digits
    if special_flag:
        characters += string.punctuation
    
    # join - string is inserted in between each joined string
    password = ''.join(random.choice(characters) for i in range(password_length))

    return password

def main():

    print('ALLSAFE password generator')
    generate_next = 'y'

    while generate_next:
        password_length = int(input('enter password length: '))
        upper_flag = input('include UPPERCASE letters? (y/n):').lower() == 'y'
        digits_flag = input('include d1g1ts? (y/n):').lower() == 'y'
        special_flag = input('include $p#c!al_s!gns? (y/n):').lower() == 'y'

        password = generate_password(password_length, upper_flag, digits_flag, special_flag)
        print(password)
        generate_next = input('generate another password? (y/n):') == 'y'

    print('bye!')

if __name__ == "__main__":
    main()