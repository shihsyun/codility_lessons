"""
Task:FrogRiverOne
Find the earliest time when a frog can jump to the other side of a river.

A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.

The goal is to find the earliest time when the frog can jump to the other side of the river. The frog can cross only when leaves appear at every position across the river from 1 to X (that is, we want to find the earliest moment when all the positions from 1 to X are covered by leaves). You may assume that the speed of the current in the river is negligibly small, i.e. the leaves do not change their positions once they fall in the river.

For example, you are given integer X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
In second 6, a leaf falls into position 5. This is the earliest time when leaves appear in every position across the river.

Write a function:

def solution(X, A)

that, given a non-empty array A consisting of N integers and integer X, returns the earliest time when the frog can jump to the other side of the river.

If the frog is never able to jump to the other side of the river, the function should return −1.

For example, given X = 5 and array A such that:

  A[0] = 1
  A[1] = 3
  A[2] = 1
  A[3] = 4
  A[4] = 2
  A[5] = 3
  A[6] = 5
  A[7] = 4
the function should return 6, as explained above.

Write an efficient algorithm for the following assumptions:

N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingYWVPQ9-8JJ/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    # 建立一個陣列n紀錄A各元素值出現的最早時間，當n除[0]皆有值>0時，回傳該陣列最大值，否則回傳-1。
    # 因為testcase 4 需要將陣列初始值設為-1

    n = [-1] * (X + 1)

    for idx ,i in enumerate(A):
        if n[i] == -1:
            n[i] = idx
        else:
            continue

    if -1 not in n[1:]:
        return max(set(n))

    return -1
   
# testcase 1
X = 5
A = [1 ,3 ,1 ,4 ,2 ,3, 5, 4]
print(solution(X , A))

# testcase 2
X = 2
A = [2 ,2 ,2 ,2]
print(solution(X , A))

# testcase 3
X = 3
A = [1, 3, 1, 3, 2, 1, 3]
print(solution(X , A))

# testcase 4
X = 1
A = [1]
print(solution(X , A))
