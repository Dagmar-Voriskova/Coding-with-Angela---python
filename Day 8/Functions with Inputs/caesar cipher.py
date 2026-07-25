import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


def caesar():

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction == 'encode':
        text = input("Type your message:\n").lower()
        shift = input("Type the shift number:\n")
        if shift.isdigit():
            shift = int(shift)
            encrypt(text, shift)
            restart()
        else:
            print("While asking for a shift number an actual number is requested.")
            restart()

    elif direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = input("Type the shift number:\n")
        if shift.isdigit():
            shift = int(shift)
            decrypt(text, shift)
            restart()
        else:
            print("While asking for a shift number an actual number is requested.")
            restart()
    else:
        print("Wrong input. Please enter 'encode' or 'decode'")
        restart()

def encrypt(original_text, shift_amount):
    text_list = []
    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index + shift_amount) % len(alphabet)
            text_list += alphabet[new_index]
        else:
            text_list += letter
    print(''.join(text_list))

def decrypt(original_text, shift_amount):
    text_list = []
    for letter in original_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            new_index = (index - shift_amount) % len(alphabet)
            text_list += alphabet[new_index]
        else:
            text_list += letter
    print(''.join(text_list))

def restart():
    restart_input = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart_input == "yes":
        caesar()
    elif restart_input == "no":
        print("Thank you for using this program.")
    else:
        print("Wrong input. Please enter 'yes' or 'no'.")



caesar()




