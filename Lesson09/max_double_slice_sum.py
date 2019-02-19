"""
Task:MaxDoubleSliceSum
Find the maximal sum of any double slice.

A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingYHF7BW-4BN/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(A):

    # write your code in Python 3.6
    # 比MaxSlice多一個變數去紀錄左邊slice總和，使用A[Z-2]代表Ｘ、A[Z-1]代表Y，取最大值後回傳
    # more detail please check it out at https://codesays.com/2014/solution-to-max-double-slice-sum-by-codility/#comment-870 .

    L_slice, until_now, once_total = 0, 0, 0

    for Z in range(3, len(A)):
        L_slice = max(0, A[Z-2] + L_slice)
        until_now = max(L_slice, A[Z-1] + until_now)
        once_total = max(until_now, once_total)

    return once_total

#testcase 1
A = [3, 2, 6, -1, 4, 5, -1, 2]
print(solution(A))

#testcase 2
A = [5, 17, 0, 3]
print(solution(A))