"""
Task:CommonPrimeDivisors
Check whether two numbers have the same prime divisors.

A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

N = 15 and M = 75, the prime divisors are the same: {3, 5};
N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.
Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:

    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5
the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Write an efficient algorithm for the following assumptions:

Z is an integer within the range [1..6,000];
each element of arrays A, B is an integer within the range [1..2,147,483,647].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingEV3KA3-J6T/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def check(N, prime_table):
    
    factor = set()

    if N == 1:
        return factor

    if N == 2:
        factor.add(N)

    for idx in range(N+1):
        if prime_table[idx]:
            if N % idx == 0:
                factor.add(idx)

    return factor


def solution(A, B):
    # write your code in Python 3.6
    # 先取A,B兩陣列的最大值做出質數表與產生檢查結果陣列result
    # 依序判斷A,B各元素是不是質數，若兩者相異又各是質數，則result紀錄為False
    # 若A,B元素皆不是質數，則利用質數表分別對元素檢查質數因數並紀錄成集合，對集合做差集，
    # 若不為空集合則result紀錄為False，count result後回傳。
    # codility回報記憶體錯誤如下，拿到38%。
    # stderr:
    #   Traceback (most recent call last):
    #       File "exec.py", line 139, in <module>
    #       main()
    #       File "exec.py", line 101, in main
    #       result = solution( A, B )
    #       File "/tmp/solution.py", line 28, in solution
    #       prime_table = [False]*2+[True]*(num_max-1)
    #       MemoryError

    N = len(A)
    num_max = max(max(A), max(B))
    prime_table = [False]*2+[True]*(num_max-1)
    result = [False]*N

    idx = 2
    while idx**2 <= num_max:
        i = 2
        while idx * i <= num_max:
            prime_table[idx*i] = False
            i += 1
        idx += 1

    for idx in range(N):
        if A[idx] == B[idx]:
            result[idx] = True
            continue

        if prime_table[A[idx]] and prime_table[B[idx]]:
            result[idx] = False
            continue

        if A[idx] > B[idx]:
            if len(check(A[idx], prime_table) - check(B[idx], prime_table)) == 0:
                result[idx] = True
        else:
            if len(check(B[idx], prime_table) - check(A[idx], prime_table)) == 0:
                result[idx] = True

    return result.count(True)

# testcase 1
A = [15, 10, 3]
B = [75, 30, 5]
print(solution(A, B))

# testcase 2
A = [2, 1, 2]
B = [1, 2, 2]
print(solution(A, B))

# testcase 3
A = [3, 9, 20, 11]
B = [9, 81, 5, 13]
print(solution(A, B))