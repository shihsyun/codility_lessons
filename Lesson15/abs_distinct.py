"""
Task:AbsDistinct
Compute number of distinct absolute values of sorted array elements.

A non-empty array A consisting of N numbers is given. The array is sorted in non-decreasing order. The absolute distinct count of this array is the number of distinct absolute values among the elements of the array.

For example, consider array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
The absolute distinct count of this array is 5, because there are 5 distinct absolute values among the elements of this array, namely 0, 1, 3, 5 and 6.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N numbers, returns absolute distinct count of array A.

For example, given array A such that:

  A[0] = -5
  A[1] = -3
  A[2] = -1
  A[3] =  0
  A[4] =  3
  A[5] =  6
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647];
array A is sorted in non-decreasing order.
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/training95SW9A-8ZX/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
def solution(A):
    # write your code in Python 3.6
    # 對A取絕對值再取集合

    for idx in range(len(A)):
        A[idx] = abs(A[idx])

    return len(set(A))


# testcase 1
A = [-5, -3, -1, 0, 3, 6]
print(solution(A))