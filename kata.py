def tail(string):
    return string[1:]

def revert(string):
    return string[::-1]

def simetrize(string):
    return string + tail(revert(string))
