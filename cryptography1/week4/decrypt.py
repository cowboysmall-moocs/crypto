import urllib2
import sys


TARGET      = "http://crypto-class.appspot.com/po?er="
CYPHER_TEXT = "f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4"
BLOCK_SIZE  = 16


def make_request(q):
    try:
        urllib2.urlopen(urllib2.Request(TARGET + urllib2.quote(q)))
    except urllib2.HTTPError, e:          
        return e.code == 404

def unencode_to_array(s):
    return [ord(c) for c in s.decode('hex')]

def xor(a, b):
    return [aa ^ bb for aa, bb in zip(a, b)]

def three_xor(a, b, c):
    return xor(a, xor(b, c))

def create_padding(index, pad):
    return [0] * index + [pad] * pad + [0] * BLOCK_SIZE

def clear_discovered(discovered, block, length):
    return discovered[:block * BLOCK_SIZE] + [0] * (length - (block * BLOCK_SIZE))

def convert_to_string(array):
    return "".join([chr(c) for c in array])

def decrypt_from_padding_oracle(cypher_text):
    length      = len(cypher_text)
    block_count = length / BLOCK_SIZE
    discovered  = [0] * length

    for block in reversed(range(1, block_count)):
        for byte in reversed(range(BLOCK_SIZE)):
            index = ((block - 1) * BLOCK_SIZE) + byte
            for guess in range(256):
                sys.stdout.write('[%d, %2d] trying byte \'%02x\' at pos %2d:\r' % (block, byte, guess, index))
                sys.stdout.flush()

                discovered[index] = guess
                cleared = clear_discovered(discovered, block, length)
                padded  = create_padding(index, BLOCK_SIZE - byte)

                if make_request(convert_to_string(three_xor(cypher_text, cleared, padded)).encode('hex')):
                    sys.stdout.write('[%d, %2d] trying byte \'%02x\' at pos %2d: %s\r' % (block, byte, guess, index, convert_to_string(discovered)))
                    sys.stdout.flush()
                    break

                if guess == 255:
                    discovered[index] = BLOCK_SIZE - byte

    return discovered


def main():
    print "Padding Oracle Demo\n"

    unencoded  = unencode_to_array(CYPHER_TEXT)
    discovered = decrypt_from_padding_oracle(unencoded)

    print "\n\nFound: ",convert_to_string(discovered)
    print "\n(hex): ",convert_to_string(discovered).encode('hex')


if __name__ == "__main__":
    main()
