import random
import string
import numpy

def create_password(password_length, characters_to_include):
    """
    args: (
        password_length: integer
        characters_to_include: list with possible items ["number", "lower", "upper", "special"]
    )

    uses random module to genereate a random password

    returns: string of length password_length
    """

    # possible characters
    number_range = list(range(0,10))
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    special_characters = ['!', '@', '&', '$', '*']

    # create character_list
    character_map = {"number": number_range, "lower": lower_case, "upper": upper_case, "special": special_characters}
    
    character_list = []
    for list_name, char_list in character_map.items():
        if list_name in characters_to_include:
            character_list += char_list

    # generate password
    password = ''
    for i in range(0, password_length):
        # create randomized index to reference character_list
        # len(character_list) - 1 is becuase len() starts at one but need the index from zero
        random_index = random.randint(0, len(character_list) - 1) 

        random_char = str(character_list[random_index])
        password += random_char

    return password

if __name__ == '__main__':
    pw = create_password(16, ["number", "lower", "upper", "special"])
    print(pw)


