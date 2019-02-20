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

You can check it out the result at https://app.codility.com/demo/results/trainingFT9KYT-V5Q/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(A):
    # write your code in Python 3.6
    # 假設前提是每一個peak都有一個block，此時的blocks數為最多。
    # 故先找出peak的數目與index，接著依序計算len(A)/peak數字序列，找出可整除的分組長度
    # 依序計算peak是否落在block內，並檢測是否每個block都有peak，若有就回傳block數目
    # more detail please check it out at https://www.martinkysel.com/codility-peaks-solution/ .

    N = len(A)
    if N < 3: return 0
    peaks = []

    for idx in range(1, N-1):
        if A[idx-1] < A[idx] > A[idx+1]:
            peaks.append(idx)

    for size in range(len(peaks), 0, -1):
         if N % size == 0:

            block_len = N // size
            check = [0]*size
            for elem in peaks:
                ptr = elem // block_len
                if check[ptr] == 0:
                    check[ptr] = 1

            if check.count(1) == size:
                return size

    return 0

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