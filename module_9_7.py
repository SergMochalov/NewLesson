def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        if n < 2:
            res = 'не простое и не сложное число'
        elif n == 2:
            res = 'Простое число'
        else:
            f = n ** (1 / 2)
            for a in range(2, int(f + 1)):
                if n % a == 0:
                    res = 'Составное число'
                else:
                    res = 'Простое число'
        print(res)
        return n
    return wrapper

@is_prime
def sum_three(a: int, b: int, c: int):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)