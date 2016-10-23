def tail(string):
    return string[1:]

def revert(string):
    return string[::-1]

def mirror(string):
    return string + tail(revert(string))
