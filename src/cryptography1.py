#!/usr/bin/env python

import sys


def week1():
    from week1 import decrypt
    decrypt.main()

def week2():
    from week2 import decrypt
    decrypt.main()

def week3():
    from week3 import hash
    hash.main()

def week4():
    from week4 import decrypt
    decrypt.main()

def week5(version = 'gmpy2'):
    if version == 'gmpy2':
        from week5.gmpy2 import discrete_log
        discrete_log.main()
    elif version == 'numbthy':
        from week5.numbthy import discrete_log
        discrete_log.main()

def week6():
    from week6 import factorize
    factorize.main()


options = {
    'week1': week1,
    'week2': week2,
    'week3': week3,
    'week4': week4,
    'week5': week5,
    'week6': week6
}


def main(argv):
    if len(argv) == 1:
        options[argv[0]]()
    else:
        options[argv[0]](argv[1])


if __name__ == "__main__":
    main(sys.argv[1:])
