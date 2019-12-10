# Caesar Cipher

import random
MAX_KEY_SIZE = 26


def get_mode():
    while True:
        print('Do you wish to encrypt or decrypt a message? Enter either "encrypt" or "e" or "decrypt" or "d"')
        mode = raw_input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d"')


def get_message():
    print('Enter your message:')
    return raw_input()


def get_key():
    print "Enter the key between 1-%s" % MAX_KEY_SIZE
    key = int(raw_input())
    return key


def get_translated_message(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            alpha_key = key % 26
            num = ord(symbol)
            num += alpha_key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        elif symbol.isdigit():
            # print "We got digit %s" % symbol
            digit_key = key % 10
            num = ord(symbol)
            num += digit_key
            if not chr(num).isdigit():
                num = num - 10
            translated += chr(num)
        else:
            translated += symbol
    return translated


if __name__ == "__main__":
    mode = get_mode()
    message = get_message()
    key = get_key()
    print ("Key is %s" % key)

    print('Your translated text is:')
    print(get_translated_message(mode, message, key))

