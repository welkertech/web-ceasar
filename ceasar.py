import string

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def return_letter(index):
    alphabet = string.ascii_uppercase
    return(alphabet.upper()[index])

def encrypt(text, rot):

    encrytString = ""
    for i in text:
        if i.isalpha():
            encrytString = encrytString + rotate_character(i,rot)
        else:
            encrytString = encrytString + i
    return(encrytString)

def alphabet_position(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter = str(letter.upper())
    alphabet = string.ascii_uppercase
    return (alphabet.index(letter))

def rotate_character(char, rot):

    rotIndex = (alphabet_position(char) + rot) % 26
    if char.islower():
        #rotIndex = (alphabet_position(char) + rot) % 26
        return (return_letter(rotIndex).lower())
    if char.isupper():
        #rotIndex = (alphabet_position(char) + rot) % 26
        return (return_letter(rotIndex).upper())
    else:
        return(char)
