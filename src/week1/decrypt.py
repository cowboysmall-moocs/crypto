import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import common
import mtp


def main(argv):
    cypher_texts = [common.hex_to_ascii(cypher_text) for cypher_text in files.read_lines(argv[0])]
    key          = mtp.find_key(cypher_texts, len(cypher_texts[10]))

    plain_text   = common.string_to_ascii('The secret message is: When using a stream cipher, never use the key more than once')
    new_key      = common.xor(plain_text, cypher_texts[10])


    print
    print 'Decrypt Many-time Pad Demo'
    print
    for i in range(len(cypher_texts)):
        print 'Message %2d = %s' % ((i + 1), ''.join([chr(c) for c in common.xor(cypher_texts[i], key)]))
    print
    print
    print 'Make best guess and use to derive key'
    print
    for i in range(len(cypher_texts)):
        print 'Message %2d = %s' % ((i + 1), ''.join([chr(c) for c in common.xor(cypher_texts[i], new_key)]))
    print


if __name__ == "__main__":
    main(sys.argv[1:])
