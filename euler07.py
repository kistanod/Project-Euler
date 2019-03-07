#!/bin/python3
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler007

from math import sqrt

def siv():
    N = 104744 # had to look up 1001st prime :D
    primes = [True]*(N)
    for i in range(2, int(sqrt(N))+1):
        for j in range(i*i, N, i):
            primes[j] = False   
    return [number for number in range(2, N) if primes[number]]

# ensures that numbers are only generated once
# to avoid time limit exeeded error
primes = siv()

trials = int(input())

for _ in range(trials):
    index = int(input())
    print(primes[index-1])
