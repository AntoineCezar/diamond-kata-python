from string import ascii_letters


def tail(string):
    return string[1:]


def reverse(string):
    return string[::-1]


def mirror(string):
    return string + tail(reverse(string))


def diamond_letters(letter):
    last_letter_position = ascii_letters.find(letter) + 1
    return ascii_letters[:last_letter_position]


def erease_when_not(letter):
    return lambda candidate: candidate if candidate == letter else ' '


def erease_other_letters(letter, string):
    return ''.join(map(erease_when_not(letter), string))


def diamond_lines(letter):
    lines = []
    letters = reverse(diamond_letters(letter))

    for letter in reverse(letters):
        partial_line = erease_other_letters(letter, letters)
        line = mirror(partial_line)
        lines.append(line)

    return mirror(lines)
