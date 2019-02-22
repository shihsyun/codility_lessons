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

You can check it out the result at https://app.codility.com/demo/results/training3DPZED-C6W/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(y, x % y)



def solution(A, B):
    # write your code in Python 3.6
    # 先對A[idx]與B[idx]取最大公因數為X，接著再取X與A[idx]的最大公因數d，如果d不是1，則a=a/d後再求最大公因數以
    # 去除非質數因數；接著取X與B[idx]的最大公因數d，如果d不是1則b=b/d去除非質數因數。
    # 以上兩個若皆為1則A[idx]與B[idx]有相同的質數因數。
    # more detail please check it out at https://codesays.com/2014/solution-to-common-prime-divisors-by-codility/#comment-1258 .

    count = 0
    for a,b in zip(A, B):
        x = gcd(a,b)
        
        while True:
            d = gcd(x, a)
            if d == 1:
                break
            a /= d

        while True:
            d = gcd(x, b)
            if d == 1:
                break
            b /= d
            
        count  += 1 if a == 1 and b == 1 else 0

    return count

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