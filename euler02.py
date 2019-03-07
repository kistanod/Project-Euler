# second problem of Project Euler
# used dynamic programming strategy 
# used pypy2 to avoid time limit exeeded 
# link: https://www.hackerrank.com/contests/projecteuler/challenges/euler002


def gen_fibs(N):
    fibs = [1,1]
    
    while fibs[-1] < N:
        fibs.append(fibs[-1]+fibs[-2])
    
    del fibs[-1]
    del fibs[1]
    return fibs

for _ in range(int(raw_input())):
    N = int(raw_input())
    total = 0
    fibs = gen_fibs(N)
    
    for index in range(1, len(fibs), 3):
        total += fibs[index]
    
    print(total)
