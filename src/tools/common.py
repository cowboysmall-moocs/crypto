

def string_to_ascii(s):
    return [ord(c) for c in s]


def hex_to_ascii(s):
    return [ord(c) for c in s.decode('hex')]


def xor(a, b):
    return [aa ^ bb for aa, bb in zip(a, b)]



