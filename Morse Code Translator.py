#https://en.wikipedia.org/wiki/Morse_code#/media/File:International_Morse_Code.svg
morse_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': ' '}

def encrypt(message):
    
    morse_code = ''
    for char in message.upper():
        if char in morse_dict:
            morse_code += morse_dict[char] + ' '
    return morse_code

def decrypt(morse_code):
    message = ''
    morse_code = morse_code.split(' ')
    for code in morse_code:
        if code == '':
            message += ' '
        else:
            for char, morse in morse_dict.items():
                if morse == code:
                    message += char
    return message

InvalidInput = True
while InvalidInput is True:
    AorB = str(input("Hello! Would you like to encrypt or decrypt a piece of text?\n(A)Encrypt\n(B)Decrypt\n").upper())
    
    if AorB == "A":
        InvalidInput = False
        break
    if AorB == "B":
        InvalidInput = False
        break
    else:
        InvalidInput = True


if AorB == "A":
    message = input("Please enter the piece of text you would like to ENCRYPT: ")
    print("The message you have entered: ", message, "\nEncrypted in Morse: ", encrypt(message))
    

if AorB == "B":
    morse_code = input("Please enter the piece of text you would like to DECRYPT: ")
    print("The encrypted message you have entered: ", morse_code, "\nDecrypted from Morse: ", decrypt(morse_code))