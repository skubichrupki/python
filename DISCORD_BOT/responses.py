import random
import time

names_buy = []
names_get = []

# user message as parametr
def handle_response(user_message) -> str:
    lower_user_message = user_message.lower()
    print(f'lowercased Message: {lower_user_message}')  # Add this line for debugging
    rand_num_buy = 0

    if 'patus' in lower_user_message:
        return 'Утро вечера мудренее. (Rano ma więcej mądrości niż wieczór.)'
    
    elif 'ocen' in lower_user_message:
        randomNum = random.randint(1,10)
        if randomNum < 5:
            return f'{randomNum}/10, takze slabiutko'
        else:
            return f'{randomNum}/10'
        

    elif lower_user_message == 'losowanie':
        return "Podaj imiona, oddzielając je przecinkami, pisząc: \n dodaj do losowania:michu, kichu, smichu."
    
    elif lower_user_message.startswith('dodaj do losowania:'):
        # Extract names from the user's message
        provided_names = user_message.split(':')[1].strip()
        # Split the names based on commas
        provided_names_separated = [name.strip() for name in provided_names.split(',')]

        names_buy.extend(provided_names_separated)
        names_get.extend(provided_names_separated)
        return f'dodalem ludzi do listy: {names_buy}'
    
    elif 'kto losuje?' in lower_user_message:
        rand_num_buy = random.randint(0, len(names_buy) - 1)
        return f'{names_buy[rand_num_buy]}, losujesz :)))'
    
    elif 'losuj' in lower_user_message:

        while True:
            rand_num_get = random.randint(0, len(names_get) - 1)
            if names_buy[rand_num_buy] != names_get[rand_num_get]:
                break

        text1 =  f'{names_buy[rand_num_buy]}, robisz prezent {names_get[rand_num_get]}'
        names_buy.pop(rand_num_buy)
        names_get.pop(rand_num_get)
        text2 = f'nie wylosowali jeszcze {", ".join(names_buy)}'
        text3 = f'DO WYJEBANIA -> nie zostali wylosowani jeszcze {", ".join(names_get)}'

        return f'{text1}\n\n{text2}\n\n{text3}'
    
    else:
        return