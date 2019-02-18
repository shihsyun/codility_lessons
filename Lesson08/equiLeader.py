"""
Task:EquiLeader
Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N - 1] are the same.

A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/training4PGZ75-8WB/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

from collections import Counter

def solution(A):

    # write your code in Python 3.6
    # 利用Counter物件計算Candidate與Candidate_count
    # 再跑一次for迴圈，計算candidate在左邊與右邊皆為leader的出現次數
    # more detail please check it out at https://codesays.com/2014/solution-to-equi-leader-by-codility/#comment-831 .

    result = 0
    candidate, candidate_count  = Counter(A).most_common()[0]

    
    left = 0
    for idx, value in enumerate(A):
            
        if value == candidate:
            left += 1
            
        if left > (idx + 1) // 2 and (candidate_count - left) > (len(A) - (idx + 1)) // 2:
            result +=1

    return result


# testcase 1
A = [4, 3, 4, 4, 4, 2]
print(solution(A))

# testcase 2
A = [1]
print(solution(A))

# testcase 3
A = [4, 3, 4, 4, 4, 2, 3]
print(solution(A))

# testcase 4
A = [1, 2, 1, 1, 2, 1]
print(solution(A))