from Crypto.Hash import SHA256


def calculate(blocks):
    current = 0

    for block in reversed(blocks):

        sha256 = SHA256.new()
        if current != 0:
            sha256.update(block + current)
        else:
            sha256.update(block)
        current = sha256.hexdigest().decode('hex')

    return current.encode('hex')

