"""
Task:ChocolatesByNumbers
There are N chocolates in a circle. Count the number of chocolates you will eat.

Two positive integers N and M are given. Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

You stop eating when you encounter an empty wrapper.

For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

The goal is to count the number of chocolates that you will eat, following the above rules.

Write a function:

def solution(N, M)

that, given two positive integers N and M, returns the number of chocolates that you will eat.

For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..1,000,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/training352773-EMT/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def solution(N, M):
    # write your code in Python 3.6
    # 求N與M的最大公因數X後，回傳N/X
    # 參考官方教材 https://codility.com/media/train/10-Gcd.pdf

    X = gcd(N, M)

    return int(N / X)


# testcase 1
N = 10
M = 4
print(solution(N, M))

# testcase 2
N = 1
M = 1
print(solution(N, M))

# testcase 3
N = 10E8
M = 5E8
print(solution(N, M))
