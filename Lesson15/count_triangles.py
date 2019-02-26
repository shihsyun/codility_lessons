"""
Task:CountTriangles
Count the number of triangles that can be built from a given set of edges.

An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if it is possible to build a triangle with sides of lengths A[P], A[Q] and A[R]. In other words, triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
There are four triangular triplets that can be constructed from elements of this array, namely (0, 2, 4), (0, 2, 5), (0, 4, 5), and (2, 4, 5).

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the number of triangular triplets in this array.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 12
the function should return 4, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000];
each element of array A is an integer within the range [1..1,000,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingTP63YD-484/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
def solution(A):
    # write your code in Python 3.6
    # 依照題目，使用迴圈count，複雜度為O(N**3)
    # 依照官方教材，複雜度降為O(N**2)
    # more detail please check it out at https://codility.com/media/train/13-CaterpillarMethod.pdf .

    N = len(A)
    count = 0
    
    A.sort()
    for x in range(N):
        z = x + 2
        for y in range(x + 1, N):
            while z < N  and A[x] + A[y] > A[z]:
                z += 1    
            count += z - y - 1

    return count

# testcase 1
A = [10, 2, 5, 1, 8, 12]
print(solution(A))