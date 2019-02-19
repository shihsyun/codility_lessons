"""
Task:
MinPerimeterRectangle
Find the minimal perimeter of any rectangle whose area equals N.

An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingJ75WFC-ZUH/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

from math import sqrt

def solution(N):
    # write your code in Python 3.6
    # 改使用sqrt，直接計算後回傳。
    # more detail please check it out at https://codesays.com/2014/solution-to-min-perimeter-rectangle-by-codility/.

    for i in range(int(sqrt(N)), 0, -1):
        if N % i == 0:
            return (int(N / i) + i) * 2

# testcase 1
N = 30
print(solution(N))

# testcase 2
N = 1
print(solution(N))

# testcase 3
N = 2
print(solution(N))

# testcase 4
N = 100
print(solution(N))

# testcase 5
N = 5
print(solution(N))

# testcase 6
N = 36
print(solution(N))

# testcase 7
N = 7
print(solution(N))

# testcase 8
N = 10E8
print(solution(N))

# testcase 9
N = 48
print(solution(N))

# testcase 10
N = 1234
print(solution(N))