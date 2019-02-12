"""
Task:PermMissingElem
Find the missing element in a given permutation.

An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/training6B4P3V-QXJ/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    # N is an integer within the range [0..100,000]
    # each element of array A is an integer within the range [1..(N + 1)]
    # 先設定回傳值為N+1，依照題目定義其值為固定的A陣列長度+1
    # 再將其依序對1~N+1與取出A的元素做XOR運算，即可找出A陣列中漏掉的整數。
    result = len(A)+1
    for N in range(0,len(A)):
        result ^= (N+1) ^ A[N]

    return result

A=[2 ,3 ,1 ,5]
print(solution(A))
