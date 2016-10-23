def revert(string):
    return string[::-1]

def simetrize(string):
    return string + revert(string)[1:]
