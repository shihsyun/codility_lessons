"""
Task:PermCheck
Check whether array A is a permutation.

A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

def solution(A)

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingF8TRG7-CSW/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # 對A做排序，依序判斷是否為有序排列
    # 若X[0]的值不為1，則回傳0
    X = sorted(A)

    if X[0] != 1:
        return 0

    for index in range(0, len(X)-1):
        if X[index]+1 != X[index+1]:
            return 0

    return 1

# testcase 1
A = [4 ,1 ,3, 2]
print(solution(A))

# testcase 2
A = [4 ,1 ,3]
print(solution(A))

# testcase 3
A = [2]
print(solution(A))