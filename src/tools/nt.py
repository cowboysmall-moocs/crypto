from gmpy2   import powmod, t_mod, invert, isqrt, mul
from numbthy import powmod, invmod


def factorize(number, delta):
    for i in xrange(1, delta + 1):
        square_root     = isqrt(number)
        average         = square_root + i
        average_squared = mul(average, average)

        x = isqrt(average_squared - number)
        p = (average - x)
        q = (average + x)

        if mul(p, q) == number:
            return (p, q, i)

    return (0, 0, 0)


def discrete_log_gmpy2(P, G, H):
    lookup   = {}

    g_to_b   = powmod(G, 1048576, P)
    g_invert = invert(G, P)

    calc_1   = t_mod(H * G, P)
    for i in xrange(1048576 + 1):
        calc_1 = t_mod(calc_1 * g_invert, P)
        lookup[calc_1] = i

    calc_0   = invert(g_to_b, P)
    for j in xrange(1048576 + 1):
        calc_0 = t_mod(calc_0 * g_to_b, P)
        if calc_0 in lookup:
            return (j * 1048576) + lookup[calc_0]

    return None


def discrete_log_numbthy(P, G, H):
    lookup   = {}

    g_to_b   = powmod(G, 1048576, P)
    g_invert = invmod(G, P)

    calc_1   = powmod(H * G, 1, P)
    for i in xrange(1048576 + 1):
        calc_1 = powmod(calc_1 * g_invert, 1, P)
        lookup[calc_1] = i

    calc_0   = invmod(g_to_b, P)
    for j in xrange(1048576 + 1):
        calc_0 = powmod(calc_0 * g_to_b, 1, P)
        if calc_0 in lookup:
            return (j * 1048576) + lookup[calc_0]

    return None

