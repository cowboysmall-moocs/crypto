import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import encdec


'''

    Decrypted Messages:

    1: Basic CBC mode encryption needs padding.\x08\x08\x08\x08\x08\x08\x08\x08
    2: Our implementation uses rand. IV\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10
    3: CTR mode lets you build a stream cipher from a block cipher.
    4: Always avoid the two time pad!

'''

def main(argv):
    lines = [line.decode('hex') for line in files.read_lines(argv[0])]


    print
    print 'AES Demo'
    print
    print encdec.aes_decrypt(lines[0], lines[1])
    print encdec.aes_decrypt(lines[0], lines[2])
    print
    print encdec.aes_decrypt(lines[3], lines[4], True)
    print encdec.aes_decrypt(lines[3], lines[5], True)
    print


if __name__ == "__main__":
    main(sys.argv[1:])
