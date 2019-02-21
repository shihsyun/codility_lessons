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

You can check it out the result at https://app.codility.com/demo/results/trainingZCFDHY-K9V/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

from math import sqrt

def solution(N, P, Q):
    # write your code in Python 3.6
    # 先計算N的平方根內所有質數，再依序計算出所有半質數陣列
    # 再利用陣列填值法求出P&Q的差距後回傳
    # 可參考官方教材 https://codility.com/media/train/9-Sieve.pdf
    # 複雜度為O(N * log(log(N)) + M * N) or O(M * N**3) or O(M * N ** (3/2))，拿到55%。
    
    max_num = int(sqrt(N)) + 1
    prime = list((range(2, N)))
    semi_prime = []
    result = []
    
    for idx in range(2, max_num):
        i = 2
        while (idx * i) < N:
            try:
                total  = idx * i
                i += 1
                prime.remove(total)
            except:
                continue

    for num in prime:
        for elem in prime:
            tmp = num * elem
            if tmp <= N:
                if tmp not in semi_prime: 
                    semi_prime.append(tmp)
            else:
                continue
        
    semi_prime.sort()
    
    for idx in range(len(P)):
        distances = [0]*len(semi_prime)
        for i in range(len(semi_prime)):
            if P[idx] <= semi_prime[i] <= Q[idx]:
                distances[i] = 1

        result.append(distances.count(1))


    return result

# testcase 1
N = 26
P = [1, 4, 16]
Q = [26, 10, 20]
print(solution(N, P, Q))
