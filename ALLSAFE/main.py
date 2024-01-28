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
    
    # join - string is inserted in between each joined string
    password = ''.join(random.choice(characters) for i in range(password_length))

    return password

def main():

    password = generate_password(3,1,1,1)
    print(password)

if __name__ == "__main__":
    main()