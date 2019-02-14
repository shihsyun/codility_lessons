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

You can check it out the result at https://app.codility.com/demo/results/training7K4WDG-JFW/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A ,B ,K):
    # write your code in Python 3.6
    # Ａ或B-A能由K整除時須加1，拿到87%分數
    # 錯誤訊息為 A = 101, B = 123M+, K = 10K got 12346 expected 12345

    X = 0 if ((B - A) % K) == 0 else 1

    if A % K == 0:
        X = 1

    return int((B - A) / K) + X

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