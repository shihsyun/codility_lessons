"""
Task:NailingPlanks
Count the minimum number of nails that allow a series of planks to be nailed.

You are given two non-empty arrays A and B consisting of N integers. These arrays represent N planks. More precisely, A[K] is the start and B[K] the end of the K−th plank.

Next, you are given a non-empty array C consisting of M integers. This array represents M nails. More precisely, C[I] is the position where you can hammer in the I−th nail.

We say that a plank (A[K], B[K]) is nailed if there exists a nail C[I] such that A[K] ≤ C[I] ≤ B[K].

The goal is to find the minimum number of nails that must be used until all the planks are nailed. In other words, you should find a value J such that all planks will be nailed after using only the first J nails. More precisely, for every plank (A[K], B[K]) such that 0 ≤ K < N, there should exist a nail C[I] such that I < J and A[K] ≤ C[I] ≤ B[K].

For example, given arrays A, B such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10
four planks are represented: [1, 4], [4, 5], [5, 9] and [8, 10].

Given array C such that:

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
if we use the following nails:

0, then planks [1, 4] and [4, 5] will both be nailed.
0, 1, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, then planks [1, 4], [4, 5] and [5, 9] will be nailed.
0, 1, 2, 3, then all the planks will be nailed.
Thus, four is the minimum number of nails that, used sequentially, allow all the planks to be nailed.

Write a function:

def solution(A, B, C)

that, given two non-empty arrays A and B consisting of N integers and a non-empty array C consisting of M integers, returns the minimum number of nails that, used sequentially, allow all the planks to be nailed.

If it is not possible to nail all the planks, the function should return −1.

For example, given arrays A, B, C such that:

    A[0] = 1    B[0] = 4
    A[1] = 4    B[1] = 5
    A[2] = 5    B[2] = 9
    A[3] = 8    B[3] = 10

    C[0] = 4
    C[1] = 6
    C[2] = 7
    C[3] = 10
    C[4] = 2
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..30,000];
each element of arrays A, B, C is an integer within the range [1..2*M];
A[K] ≤ B[K].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingRD3JMT-WS4/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(A, B, C):
    # write your code in Python 3.6
    # 依序使用迴圈計算A[K] ≤ C[I] ≤ B[K]，count次數後回傳。

    count = 0

    i = 0
    for idx in range(len(C)):
        while i < len(A):
            if A[i] <= C[idx] <= B[i]:
                count += 1
                break
            i += 1

    if count == 0:
        return -1
    else:
        return count

# testcase 1
A = [1, 4, 5, 8]
B = [4, 5, 9, 10]
C = [4, 6, 7, 10, 2]
print(solution(A, B, C))

# testcase 2
A = [3, 4, 5, 8]
B = [4, 5, 9, 10]
C = [2]
print(solution(A, B, C))

# testcase 3
A = [1]
B = [1]
C = [1]
print(solution(A, B, C))

# testcase 4
A = [1, 1, 1]
B = [2, 2, 2]
C = [1, 2, 3]
print(solution(A, B, C))

# testcase 5
A = [1, 1, 1]
B = [2, 2, 2]
C = [3, 2, 1]
print(solution(A, B, C))