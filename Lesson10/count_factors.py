"""
Task:CountFactors
Count factors of given number n.

A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at  .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(N):

    # write your code in Python 3.6
    # 參考codility附的教材，利用平方根方式求因數。
    # more detail please check it out at https://codility.com/media/train/8-PrimeNumbers.pdf .

    count = 0
    i = 1

    while i**2 <= N:
        if N % i == 0:
            count += 2
        
        i += 1

    if i**2 == N:
        count += 1

    return count


# testcase 1
N = 24
print(solution(N))

# testcase 2
N = 1
print(solution(N))

# testcase 3
N = 2147483647
print(solution(N))

# testcase 4
N = 100
print(solution(N))