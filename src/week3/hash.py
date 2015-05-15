import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import hsh


HASH_1 = '03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8'
HASH_2 = '5b96aece304a1422224f9a41b228416028f9ba26b0d1058f400200f06a589949'


def main(argv):
    hash_1 = hsh.calculate(files.read_blocks('%s/%s' % (argv[0], '6 - 2 - Generic birthday attack (16 min).mp4')))
    hash_2 = hsh.calculate(files.read_blocks('%s/%s' % (argv[0], '6 - 1 - Introduction (11 min).mp4')))


    print
    print 'SHA256 Demo'
    print
    print 'Expected Hash: ', HASH_1
    print '  Actual Hash: ', hash_1
    print '   Successful: ', HASH_1 == hash_1
    print
    print 'Expected Hash: ', HASH_2
    print '  Actual Hash: ', hash_2
    print '   Successful: ', HASH_2 == hash_2
    print


if __name__ == "__main__":
    main(sys.argv[1:])
