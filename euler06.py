#!/bin/python3

# utilized sum up to formula for n**1 and n**2
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler006

import sys

def n_sum(N):
    return ((N)*(N + 1))//2

def n_2_sum(N):
    return (N*(N + 1)*(2*N + 1)) // 6

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print((n_sum(n)**2)-n_2_sum(n))
