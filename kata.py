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


def erease_when_not(letter):
    return lambda candidate: candidate if candidate == letter else ' '


def erease_other_letters(letter, string):
    return ''.join(map(erease_when_not(letter), string))


def diamond_lines(letter):
    lines = []
    letters = revert(diamond_letters(letter))

    for letter in revert(letters):
        to_erease = letters.replace(letter, '')
        line = mirror(erease(to_erease, letters))
        lines.append(line)

    return mirror(lines)
