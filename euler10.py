# this one took me a while
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler010/submissions/code/1311561423
# ensured everything is precomputed before asking for input

from math import sqrt

def siv():
    N = 1000001
    primes = [True]*(N)
    for i in range(2, int(sqrt(N))+1):
        for j in range(i*i, N, i):
            primes[j] = False   
    return primes

def find_sum(N, sums):
    for index in range(1, len(sums)):
        if (sums[index]-sums[index-1]) > N:
            return sums[index-1]
            
# generate primes only once
primes = siv()
sums = [2]

# add summation of primes only once
for i in range(3, 1000001):
    if primes[i]:
        sums.append(sums[-1]+i)

# with everything precomputed, solve
for _ in range(int(input())):
    N = int(input())
    print(find_sum(N, sums))
