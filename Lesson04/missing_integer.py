"""
Task:MissingInteger
Find the smallest positive integer that does not occur in a given sequence.

This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingAH3KT6-AYB/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    # write your code in Python 3.6
    # 使用set做判斷，得到分數55%

    if len(A) == 1 and A[0] > 1:
        return 1

    N = set(range(1 ,len(A)))
    X = set(A)
    
    R1 = X - N
    if R1.pop() <= 0:
        return 1

    R2 = N - X
    if len(R2) == 0:
        return len(A)+1

    return R2.pop()


# testcase 1
A = [1, 3, 6, 4, 1, 2]
print (solution(A))

# testcase 2
A = [1, 2, 3]
print (solution(A))

# testcase 3
A = [-1, -3]
print (solution(A))

# testcase 4
A = [2]
print (solution(A))


