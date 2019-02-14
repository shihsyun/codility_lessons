"""
Task:Triangle
Determine whether a triangle can be built from a given set of edges.

An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/training7ZFUDG-2M3/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
        
    # write your code in Python 3.6
    # 先將A中大於0的元素加到新陣列N，若N剩餘個數<3則回傳0
    # 排序N後掃描陣列計算N[i]+N[i+1]之和是否大於N[i+2]

    N = []
    for idx in A:
        if idx > 0:
            N.append(idx)

    if len(N) < 3:
        return 0

    N.sort()

    for i in range(len(N) - 2):
        if (N[i] + N[i+1]) > N[i+2]:
            return 1

    return 0


# testcase1
A = [10 ,2 ,5 ,1 ,8, 20]
print(solution(A))

# testcase1
A = [10 ,50 ,5 ,1]
print(solution(A))
