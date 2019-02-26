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

You can check it out the result at https://app.codility.com/demo/results/training2EPFEU-EGJ/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

    # write your code in Python 3.6
    # 查詢網路作法後，得知如果K==1時，large sum就是sum(A)，K>=len(A)時，即代表large sum是max(A)。
    # 即可依據這兩個邊界條件進行二分搜尋，找到可能的block size sum，再依據這個可能值依序掃描陣列檢驗是否能分成K個block。
    # more detail please check it out at https://www.martinkysel.com/codility-minmaxdivision-solution/ .

def check(A, K, max_block_sum):
    block_sum = 0
    count = 0

    for elem in A:
        if block_sum + elem > max_block_sum:
            block_sum = elem
            count += 1
        else:
            block_sum += elem
        
        if count >= K:
            return False

    return True


def solution(K, M, A):

    lower_bound = max(A)
    upper_bound = sum(A)

    if K == 1:
        return upper_bound

    if K >= len(A):
        return lower_bound

    while lower_bound <= upper_bound:
        possible_candidate = (lower_bound + upper_bound) // 2

        if check(A, K, possible_candidate):
            upper_bound = possible_candidate - 1
        else:
            lower_bound = possible_candidate + 1

    return lower_bound

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


