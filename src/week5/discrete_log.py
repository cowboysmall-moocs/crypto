import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../tools'))

import files
import number


'''
    x should be equal to 375374217830

'''

def main(argv):
    P, G, H    = [int(i) for i in files.read_lines(argv[0])]

    # calculated = number.discrete_log_numbthy(P, G, H)
    calculated = number.discrete_log(P, G, H)


    print
    print "Discrete Log Demo"
    print 
    print 'Successfully found x with a value of %s' % calculated
    print


if __name__ == "__main__":
    main(sys.argv[1:])
