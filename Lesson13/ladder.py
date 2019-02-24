"""
Task:Ladder
Count the number of different ways of climbing to the top of a ladder.

You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. With each step, you can ascend by one or two rungs. More precisely:

with your first step you can stand on rung 1 or 2,
if you are on rung K, you can move to rungs K + 1 or K + 2,
finally you have to stand on rung N.
Your task is to count the number of different ways of climbing to the top of the ladder.

For example, given N = 4, you have five different ways of climbing, ascending by:

1, 1, 1 and 1 rung,
1, 1 and 2 rungs,
1, 2 and 1 rung,
2, 1 and 1 rungs, and
2 and 2 rungs.
Given N = 5, you have eight different ways of climbing, ascending by:

1, 1, 1, 1 and 1 rung,
1, 1, 1 and 2 rungs,
1, 1, 2 and 1 rung,
1, 2, 1 and 1 rung,
1, 2 and 2 rungs,
2, 1, 1 and 1 rungs,
2, 1 and 2 rungs, and
2, 2 and 1 rung.
The number of different ways can be very large, so it is sufficient to return the result modulo 2P, for a given integer P.

Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of L integers, returns an array consisting of L integers specifying the consecutive answers; position I should contain the number of different ways of climbing the ladder with A[I] rungs modulo 2B[I].

For example, given L = 5 and:

    A[0] = 4   B[0] = 3
    A[1] = 4   B[1] = 2
    A[2] = 5   B[2] = 4
    A[3] = 5   B[3] = 3
    A[4] = 1   B[4] = 1
the function should return the sequence [5, 1, 8, 0, 1], as explained above.

Write an efficient algorithm for the following assumptions:

L is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..L];
each element of array B is an integer within the range [1..30].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingEDHH9G-KS2/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(A, B):
    # write your code in Python 3.6
    # 這題是計算A[i]與2**B[i]的同餘 https://zh.wikipedia.org/wiki/%E5%90%8C%E9%A4%98
    # A[i]階的可能路徑恰好是Fib[i+1] ex: 3階3種 4階5種 5階8種，故先計算出1~5000的Fib與2**30表備用
    # 接著再依序求出與B[i]的同餘後回傳即可，拿到87%，複雜度為O(L**2)
  
    max_num  = max(A)
    N = len(A)
    fib_table = [0, 1] + [-1]*max_num
    pow_table = [0]*31
    result = [0]*N

    for idx in range(2, max_num + 2):
        fib_table[idx] = fib_table[idx - 2] + fib_table[idx - 1]

    fib_table = fib_table[2:]

    for idx in range(1, 31):
        pow_table[idx] = 2**idx

    for idx in range(N):
        value = fib_table[A[idx] - 1]
        result[idx] = value % pow_table[B[idx]]

    return result

# testcase 1
A = [4, 4, 5, 5, 1]
B = [3, 2, 4, 3, 1]
print(solution(A, B))