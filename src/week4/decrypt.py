import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import encdec


def main(argv):
    cypher_text = files.read_line(argv[0])
    decrypted   = encdec.padding_oracle_decrypt(cypher_text, 'http://crypto-class.appspot.com/po', 'er')

    print
    print 'Padding Oracle Demo'
    print
    print 'Found: ', decrypted
    print
    print '  Hex: ', decrypted.encode('hex')
    print


if __name__ == "__main__":
    main(sys.argv[1:])
