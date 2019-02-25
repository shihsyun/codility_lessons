"""
Task:MinMaxDivision
Divide array A into K blocks and minimize the largest sum of any block.

You are given integers K, M and a non-empty array A consisting of N integers. Every element of the array is not greater than M.

You should divide this array into K blocks of consecutive elements. The size of the block is any integer between 0 and N. Every element of the array should belong to some block.

The sum of the block from X to Y equals A[X] + A[X + 1] + ... + A[Y]. The sum of empty block equals 0.

The large sum is the maximal sum of any block.

For example, you are given integers K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
The array can be divided, for example, into the following blocks:

[2, 1, 5, 1, 2, 2, 2], [], [] with a large sum of 15;
[2], [1, 5, 1, 2], [2, 2] with a large sum of 9;
[2, 1, 5], [], [1, 2, 2, 2] with a large sum of 8;
[2, 1], [5, 1], [2, 2, 2] with a large sum of 6.
The goal is to minimize the large sum. In the above example, 6 is the minimal large sum.

Write a function:

def solution(K, M, A)

that, given integers K, M and a non-empty array A consisting of N integers, returns the minimal large sum.

For example, given K = 3, M = 5 and array A such that:

  A[0] = 2
  A[1] = 1
  A[2] = 5
  A[3] = 1
  A[4] = 2
  A[5] = 2
  A[6] = 2
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and K are integers within the range [1..100,000];
M is an integer within the range [0..10,000];
each element of array A is an integer within the range [0..M].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingQN25HP-5QT/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(K, M, A):
    # write your code in Python 3.6
    # 按照題目要求，使用迴圈求最大值。

    result = [0]*K
    d = len(A) // K

    if d == 0: return max(A)

    for idx in range(K):
        result[idx] = A[idx*d:idx*d+d]

    total = 0
    for elem in result:
        total = max(total, sum(elem))

    return total

# testcase 1
K = 3
M = 5
A = [2, 1, 5, 1, 2, 2, 2]
print(solution(K, M, A))

# testcase 2
K = 2
M = 5
A = [5, 3]
print(solution(K, M, A))

# testcase 3
K = 3
M = 5
A = [5, 3]
print(solution(K, M, A))

# testcase 4
K = 2
M = 7
A = [4, 1, 2, 7]
print(solution(K, M, A))


