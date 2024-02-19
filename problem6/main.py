def prime_number(number):
    if number <= 1:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
    return True

def full_prima(number):
    num_digits = len(str(number))
    for _ in range(num_digits):
        digit = number % 10
        if not prime_number(digit):
            return False
        number //= 10
    return True

if __name__ == '__main__':
    print(full_prima(2)) # True
    print(full_prima(3)) # True
    print(full_prima(11)) # False
    print(full_prima(13)) # False
    print(full_prima(23)) # True
    print(full_prima(29)) # False
    print(full_prima(37)) # True
    print(full_prima(41)) # False
    print(full_prima(43)) # False
    print(full_prima(53)) # True