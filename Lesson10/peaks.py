"""
Task:Peaks
Divide an array into the maximum number of same-sized blocks, each of which should contain an index P such that A[P - 1] < A[P] > A[P + 1].

A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly three peaks: 3, 5, 10.

We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:

A[0], A[1], ..., A[K − 1],
A[K], A[K + 1], ..., A[2K − 1],
...
A[N − K], A[N − K + 1], ..., A[N − 1].
What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).

The goal is to find the maximum number of blocks into which the array A can be divided.

Array A can be divided into blocks as follows:

one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.
However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak. Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].

The maximum number of blocks that array A can be divided into is three.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.

If A cannot be divided into some number of blocks, the function should return 0.

For example, given:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingT5DHQX-QG9/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

from math import sqrt

def solution(A):
    # write your code in Python 3.6
    # 準備一個長度為len(A)的[0]陣列Ｘ，依序判斷peak後，在peak位置填入1
    # 計算len(A)的因數，並將Ｘ拆分成blocks，依序判斷blocks中是否有1，紀錄最大數目的blocks數後回傳
    # 複雜度為O(N*log(log(N)))

    N = len(A)
    X = [0]*N
    F = []
    count = 0

    if N < 3:
        return 0

    for idx in range(1, N - 1):
        if A[idx-1] < A[idx] > A[idx+1]:
            X[idx] = 1

    if not 1 in X:
        return 0

    for i in range(1, int(sqrt(N))+1):
        if N % i == 0:
            F.append(i)
            j = int(N / i)
            if N % j == 0:
                F.append(j)

    if len(F) == 2:
        return 1

    F.sort()

    for i in range(1, len(F)):
        ptr = 0
        blocks = int(N/F[i])

        for j in range(blocks):
            if 1 in X[F[i]*j:F[i]*j+F[i]]:
                ptr += 1
        
        if ptr == blocks:
            if count < blocks:
                return blocks

    return count

# testcase 1
A = [1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
print(solution(A))

# testcase 2
A = [0]
print(solution(A))

# testcase 3
A = [0, 1]
print(solution(A))

# testcase 4
A = [0, 1, 0]
print(solution(A))

# testcase 5
A = [0, 0, 0, 0, 1]
print(solution(A))

# testcase 6
A = [1, 3, 2, 1]
print(solution(A))