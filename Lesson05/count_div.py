"""
Task:CountDiv
Compute number of integers divisible by k in range [a..b].

Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/training7FYMSS-MVT/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A ,B ,K):
    # write your code in Python 3.6
    # 先計算A%K是否整除，若有須加1
    # 之後分別將B與A除以K，並計算其差後回傳
    # more detail please check it out at https://codesays.com/2014/solution-to-count-div-by-codility/#comment-1411 .

    Ｘ = 1 if (A % K) == 0 else 0
    return (B // K) - (A // K)  + X

# testcase 1
A = 6
B = 11
K = 2
print(solution(A, B, K))

# testcase 2
A = 0
B = 0
K = 11
print(solution(A, B, K))

# testcase 3
A = 10
B = 10
K = 5
print(solution(A, B, K))

# testcase 4
A = 0
B = 14
K = 2
print(solution(A, B, K))