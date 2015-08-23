import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import encdec
import number

from gmpy2 import mpz, mul, div


'''
    Decrypted Message: Factoring lets us break RSA.

'''


def main(argv):
    lines      = files.read_lines(argv[0])
    N_1        = mpz(lines[0])
    N_2        = mpz(lines[1])
    N_3        = mpz(lines[2])

    lines      = files.read_lines(argv[1])
    C          = mpz(lines[0])
    E          = int(lines[1])

    p1, q1, i1 = number.factorize(N_1, 1)
    p2, q2, i2 = number.factorize(N_2, 1048576)
    p3, q3, i3 = number.factorize(mul(N_3, 24), 1)

    print
    print 'Factorization Demo'
    print
    print '       1st:'
    print 'Iterations: ', i1
    print '         p: ', p1
    print '         q: ', q1
    print ' Plaintext: ', encdec.rsa_decrypt(C, E, p1, q1, N_1)
    print
    print '       2nd:'
    print 'Iterations: ', i2
    print '         p: ', p2
    print '         q: ', q2
    print
    print '       3rd:'
    print 'Iterations: ', i3
    print '         p: ', div(p3, 6)
    print '         q: ', div(q3, 4)
    print


if __name__ == "__main__":
    main(sys.argv[1:])
