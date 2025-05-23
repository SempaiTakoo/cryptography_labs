import random
import time

import sympy


def is_valid_curve(a, b, p):
    return (4 * pow(a, 3, p) + 27 * pow(b, 2, p)) % p != 0


def find_point_on_curve(a, b, p):
    while True:
        x = random.randint(0, p - 1)
        rhs = (pow(x, 3, p) + a * x + b) % p
        if sympy.legendre_symbol(rhs, p) == 1:
            for y in range(p):
                if (y * y) % p == rhs:
                    return (x, y)


def point_add(P, Q, a, p):
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if x1 == x2 and y1 != y2:
        return None

    if P == Q:
        m = (3 * x1 * x1 + a) * sympy.mod_inverse(2 * y1, p)
    else:
        m = (y2 - y1) * sympy.mod_inverse(x2 - x1, p)

    m %= p

    x3 = (m * m - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return (x3, y3)


def scalar_mult(k, P, a, p):
    R = None
    Q = P
    while k:
        if k & 1:
            R = point_add(R, Q, a, p)
        Q = point_add(Q, Q, a, p)
        k >>= 1
    return R


def find_order(P, a, p):
    Q = P
    order = 1

    while Q is not None:
        Q = point_add(Q, P, a, p)
        order += 1

    return order


def main():

    for p in sympy.primerange(50_000, 1000_000_000):
        for a in range(100_000, 1000_000):
            for b in range(100_000, 1000_000):
                P = find_point_on_curve(a, b, p)

                print(f'p = {p}, a = {a}, b = {b}, точка P = {P}')

                start = time.time()
                order = find_order(P, a, p)
                duration = time.time() - start

                print(f'Порядок точки: {order}, время: {duration:.2f} сек')

                if 600 <= duration <= 700:
                    print(
                        'Параметры для эллиптической кривой: \n'
                        'p = {p}, a = {a}, b = {b} \n'
                        'Точка: {P} \n'
                        'Порядок: {order}'
                    )
                    break


if __name__ == '__main__':
    main()
