import random

# random num from 1 to 10

# function for responses
# user message as parametr
def handle_response(message) -> str:
    l_message = message.lower()
    print(f'Lowercased Message: {l_message}')  # Add this line for debugging

    if 'patus' in l_message:
        return 'Утро вечера мудренее. (Rano ma więcej mądrości niż wieczór.)'
    elif 'ocen' in l_message:
        randomNum = random.randint(1,10)
        return f'{randomNum}/10'
    elif l_message == '!help':
        return '`modify this`'
    else:
        return 'test'
    