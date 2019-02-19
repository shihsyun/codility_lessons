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

You can check it out the result at https://app.codility.com/demo/results/training89782B-Y85/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(A):

    # write your code in Python 3.6
    # 將原始陣列分成左右兩個陣列，左陣列為依序計算A[1]開始至最後的元素數值總和
    # 右陣列為反向自A[-2]開始計算至最後，以上皆若遇負值需填0。
    # 最後再將左右兩陣列數值加總取最大值後回傳
    # https://en.wikipedia.org/wiki/Maximum_subarray_problem
    # more detail please check it out at https://www.martinkysel.com/codility-maxdoubleslicesum-solution/ .

    size = len(A)
    L_slice = [0]*size
    R_slice = [0]*size

    for idx in range(1, size):
        L_slice[idx] = max(0, L_slice[idx-1] + A[idx])

    for idx in reversed(range(size-1)):
        R_slice[idx] = max(0, A[idx] + R_slice[idx+1])

    once_total = L_slice[0] + R_slice[2]

    for idx in range(1, size-1):
        once_total = max(once_total, L_slice[idx-1] + R_slice[idx+1])

    return once_total

#testcase 1
A = [3, 2, 6, -1, 4, 5, -1, 2]
print(solution(A))

#testcase 2
A = [5, 17, 0, 3]
print(solution(A))