import argparse
import random


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_primes(count, seed):
    random.seed(seed)
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes


def main():
    parser = argparse.ArgumentParser(description="Генерация простых чисел.")
    parser.add_argument("count", type=int, help="Количество простых чисел для генерации")
    parser.add_argument("seed", type=int, help="Seed для генератора случайных чисел")

    args = parser.parse_args()

    primes = generate_primes(args.count, args.seed)

    for prime in primes:
        print(prime)


if __name__ == "__main__":
    main()
