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

You can check it out the result at https://app.codility.com/demo/results/trainingQ5SAJ6-ECG/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    # write your code in Python 3.6
    # 使用in語法做判斷，花費時間為O(N**2)
    for idx in range(1 ,len(A)+2):
        if idx not in A:
            return idx
    
    return idx


# testcase 1
A = [1, 3, 6, 4, 1, 2]
print (solution(A))

# testcase 2
A = [1, 2, 3]
print (solution(A))

# testcase 3
A = [-1, -3]
print (solution(A))

