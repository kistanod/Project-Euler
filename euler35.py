# project Euler, problem 35
# https://www.hackerrank.com/contests/projecteuler/challenges/euler035/copy-from/1311661401

from math import sqrt


# quickly sift through primes up to 10**6
def siv():
    N = 1000000
    primes = [True]*(N)
    for i in range(2, int(sqrt(N))+1):
        for j in range(i*i, N, i):
            primes[j] = False
    return [number for number in range(2, N) if primes[number]]


# find all rotations of a given number
def find_rotations(num):
    num = str(num)
    rotations = []
    for rotation in range(len(num)):
        temp = num[1:] + num[0]
        rotations.append(int(temp))
        num = temp
    return rotations


# given set of primes, find all circular primes
def find_circ_primes(primes):
    set_primes = set(primes)
    circular_primes = []
    for prime in primes:
        if all([item in set_primes for item in find_rotations(prime)]):
            circular_primes.append(prime)
    return circular_primes


def sum_up_to(circ_primes, N):
    for index in range(len(circ_primes)):
        if circ_primes[index] > N:
            return sum(circ_primes[:index])
    return sum(circ_primes)


if __name__ == "__main__":
    primes = siv()
    circ_primes = find_circ_primes(primes)

    N = int(input())
    result = sum_up_to(circ_primes, N)
    print(result)


