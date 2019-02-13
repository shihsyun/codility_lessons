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

You can check it out the result at https://app.codility.com/demo/results/trainingDUCFG7-2SE/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    # write your code in Python 3.6
    # 創建一完整set，長度須為len(A)+2，否則與原集合做完差集後會產生空集合。
    # https://codesays.com/2014/solution-to-missing-integer-by-codility/#comment-1536
    return min(set(range(1 ,len(A) + 2)) - set(A))


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


