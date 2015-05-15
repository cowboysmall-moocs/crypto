

def string_to_ascii(string):
    return [ord(c) for c in string]


def hex_to_ascii(string):
    return [ord(c) for c in string.decode('hex')]


def ascii_to_string(array):
    return ''.join(chr(i) for i in array)


def xor(a, b):
    return [aa ^ bb for aa, bb in zip(a, b)]


def three_xor(a, b, c):
    return xor(a, xor(b, c))



