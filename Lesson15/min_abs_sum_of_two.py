"""
Task:MinAbsSumOfTwo
Find the minimal absolute value of a sum of two elements.

Let A be a non-empty array consisting of N integers.

The abs sum of two for a pair of indices (P, Q) is the absolute value |A[P] + A[Q]|, for 0 ≤ P ≤ Q < N.

For example, the following array A:

  A[0] =  1
  A[1] =  4
  A[2] = -3
has pairs of indices (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2). 
The abs sum of two for the pair (0, 0) is A[0] + A[0] = |1 + 1| = 2. 
The abs sum of two for the pair (0, 1) is A[0] + A[1] = |1 + 4| = 5. 
The abs sum of two for the pair (0, 2) is A[0] + A[2] = |1 + (−3)| = 2. 
The abs sum of two for the pair (1, 1) is A[1] + A[1] = |4 + 4| = 8. 
The abs sum of two for the pair (1, 2) is A[1] + A[2] = |4 + (−3)| = 1. 
The abs sum of two for the pair (2, 2) is A[2] + A[2] = |(−3) + (−3)| = 6. 
Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the minimal abs sum of two for any pair of indices in this array.

For example, given the following array A:

  A[0] =  1
  A[1] =  4
  A[2] = -3
the function should return 1, as explained above.

Given array A:

  A[0] = -8
  A[1] =  4
  A[2] =  5
  A[3] =-10
  A[4] =  3
the function should return |(−8) + 5| = 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingMRQ2GU-2AF/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""
def solution(A):
    # write your code in Python 3.6
    # 依照題目使用雙迴圈，拿到36%。
    # 先將A排序，則min abs sum必定在差距最小的連續兩個數列上
    # more detail please check it out at https://www.martinkysel.com/codility-minabssumoftwo-solution/ .
    
    diff = int(20E8)
    beg = 0
    end = len(A) - 1
    A.sort()

    while beg <= end:
        diff = min(diff, abs(A[beg]+A[end]))

        if abs(A[beg]) > abs(A[end]):
          beg += 1
        else:
          end -= 1
      
    return diff

# testcase 1
A = [1, 4, -3]
print(solution(A))

# testcase 2
A = [-8, 4, 5, -10, 3]
print(solution(A))

# testcase ３
A = [0]
print(solution(A))