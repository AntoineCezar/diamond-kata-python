from string import ascii_letters

def tail(string):
    return string[1:]

def revert(string):
    return string[::-1]

def mirror(string):
    return string + tail(revert(string))

def diamond_letters(letter):
    return ascii_letters[:ascii_letters.find(letter) + 1]

def erease(chars, string):
    for char in chars:
        string = string.replace(char, ' ')
    return string
