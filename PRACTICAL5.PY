def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes(limit):
    print("Prime numbers up to", limit, ":")
    for num in range(2, limit + 1):
        if is_prime(num):
            print(num, end=" ")

limit = int(input("Enter the limit to find prime numbers: "))
print_primes(limit)
