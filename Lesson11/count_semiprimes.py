"""
Task:CountSemiprimes
Count the semiprime numbers in the given range [a..b]

A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
The number of semiprimes within each of these ranges is as follows:

(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.
Write a function:

def solution(N, P, Q)

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
the function should return the values [10, 4, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
M is an integer within the range [1..30,000];
each element of arrays P, Q is an integer within the range [1..N];
P[i] ≤ Q[i].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/training65KSQW-V2S/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(N, P, Q):
    # write your code in Python 3.6
    # 先計算N的所有質數，接著依序使用雙迴圈計算出所有半質數陣列，內迴圈需從外迴圈的idx起始做計算，大於N時需Break
    # 最後再利用prefix sum法求出Q-P-1的差距後回傳，複雜度降為O(N*log(log(N))+M)。
    # more detail please check it out at https://codesays.com/2014/solution-to-count-semiprimes-by-codility/.
    
    prime_table = [False]*2+[True]*(N-1)
    prime = []
    semi_prime = [0]*(N+1)
    result = []

    idx = 2
    while idx**2 <= N:
        i = 2
        while idx * i <= N:
            prime_table[idx*i] = False
            i += 1
        idx += 1
    
    for idx in range(len(prime_table)):
        if prime_table[idx]:
            prime.append(idx)

    for idx in range(len(prime)):
        for i in range(idx, len(prime)):
            tmp = prime[idx] * prime[i]
            if tmp <= N:
                semi_prime[tmp] = 1
            else:
                break

    for idx in range(1, N+1):
        semi_prime[idx] += semi_prime[idx-1]

    for idx in range(len(P)):
        result.append(semi_prime[Q[idx]] - semi_prime[P[idx] - 1])

    return result

# testcase 1
N = 26
P = [1, 4, 16]
Q = [26, 10, 20]
print(solution(N, P, Q))
