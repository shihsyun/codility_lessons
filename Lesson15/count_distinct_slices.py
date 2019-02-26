"""
Task:CountDistinctSlices
Count the number of distinct slices (containing only unique numbers).

An integer M and a non-empty array A consisting of N non-negative integers are given. All integers in array A are less than or equal to M.

A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The slice consists of the elements A[P], A[P + 1], ..., A[Q]. A distinct slice is a slice consisting of only unique numbers. That is, no individual number occurs more than once in the slice.

For example, consider integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
There are exactly nine distinct slices: (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2), (3, 3), (3, 4) and (4, 4).

The goal is to calculate the number of distinct slices.

Write a function:

def solution(M, A)

that, given an integer M and a non-empty array A consisting of N integers, returns the number of distinct slices.

If the number of distinct slices is greater than 1,000,000,000, the function should return 1,000,000,000.

For example, given integer M = 6 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 5
    A[3] = 5
    A[4] = 2
the function should return 9, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [0..100,000];
each element of array A is an integer within the range [0..M].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingCMXFSA-XZ5/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
def solution(M, A):
    # write your code in Python 3.6
    # 使用雙迴圈count，拿到70%。
    # 查詢網路作法後，使用Caterpillar method，先準備一個seen的boolean陣列，長度為Ｍ+1
    # 接著依序檢查A[back]是否已有出現，若有則移動back(back+=1)並把seen[A[back]]設為False
    # 反之則count+=(back-front)，並移動front與將seen[A[front]]設為True，複雜度降為O(N)
    # more detail please check it out at https://codesays.com/2014/solution-to-count-distinct-slices-by-codility/#comment-1794 .

    seen = [False]*(M+1)
    N = len(A)
    front, back, count = 0, 0, 0

    while front < N:
        if back < N and seen[A[back]] == False:
            seen[A[back]] = True
            back += 1
        else:
            count += back - front
            seen[A[front]] = False
            front += 1

    return min(count , int(10E8))
    
# testcase 1
M = 6
A = [3, 4, 5, 5, 2]
print(solution(M, A))