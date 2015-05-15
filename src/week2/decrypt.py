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
    print encdec.aes_decrypt(lines[1], lines[0])
    print encdec.aes_decrypt(lines[2], lines[0])
    print
    print encdec.aes_decrypt(lines[4], lines[3], True)
    print encdec.aes_decrypt(lines[5], lines[3], True)
    print


if __name__ == "__main__":
    main(sys.argv[1:])
