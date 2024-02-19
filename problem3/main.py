def prime_number(number):
    if number <= 1:
        return "Not Prime"
    for x in range(2, number):
        if number % x == 0:
            return "Not Prime"
    return "Prime"

if __name__ == '__main__':
    print(prime_number(11)) # "Prime"
    print(prime_number(13)) # "Prime"
    print(prime_number(17)) # "Prime"
    print(prime_number(20)) # "Not Prime"
    print(prime_number(35)) # "Not Prime"