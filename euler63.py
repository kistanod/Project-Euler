# closed form solution
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler063


from math import ceil as ceiling

n = int(input())

start = ceiling(pow(10, 1-1/n))

for i in range(start, 10):
    print(pow(i,n))
