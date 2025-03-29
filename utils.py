
def fibonacci_pow_aux(t1: int, t2: int, n: int, fib_table: list):

    if fib_table[n] >= 0:
        return fib_table[n]

    if n == 1:
        term_n = t1
    elif n == 2:
        term_n = t2
    else:
        prev_term1 = fibonacci_pow(t1, t2, n - 1)**2
        prev_term2 = fibonacci_pow(t1, t2, n - 2)
        term_n = prev_term1 + prev_term2

    fib_table[n] = term_n
    return term_n


def fibonacci_pow(t1, t2, n):
    # top-down fibonacci pow with memomization

    table = [-1 for i in range(n + 1)]
    return fibonacci_pow_aux(t1, t2, n, table)


def fibonacci_pow_bottomup(t1: int, t2: int, n: int):
    # bottom up fibonacci pow

    fib_table = [0, t1, t2] + [-1 for i in range(3, n + 1)]
    for i in range(3, n + 1):
        tnext = fib_table[i - 1]**2 + fib_table[i - 2]
        fib_table[i] = tnext

    return fib_table[n]


def fibonacci(n: int):
    # top-down fibonacci with memoization
    fib_table = [-1 for _ in range(n + 1)]
    return fibonacci_aux(n, fib_table)


def fibonacci_aux(n: int, fib_table: list):

    if fib_table[n] != -1:
        return fib_table[n]
    else:
        if n == 1:
            term = 1
        elif n == 2:
            term = 1
        else:
            first_term = fibonacci_aux(n - 1, fib_table)
            second_term = fibonacci_aux(n - 2, fib_table)
            term = first_term + second_term

        fib_table[n] = term
        return term
