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

You can check it out the result at https://app.codility.com/demo/results/trainingNPB9KB-T9H/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(A):

    # write your code in Python 3.6
    # 依照題目定義，進行迴圈比對。
    # 解法的複雜度為O(N**2)，拿到55%。

    count = 0

    for idx in range(len(A)):

        A1 = A[:idx+1]
        A2 = A[idx+1:]
        repeat = []

        for i in range(len(A1)):
            for j in range(len(A2)):
                if A1[i] == A2[j] and A1[i] not in repeat:
                    repeat.append(A1[i])

        
        for i in range(len(repeat)):
            A1times, A2times = 0, 0

            for j in range(len(A1)):
                if repeat[i] == A1[j]:
                    A1times += 1

            for j in range(len(A2)):
                if repeat[i] == A2[j]:
                    A2times += 1

            if A1times * 2 > len(A1)  and A2times * 2 > len(A2):
                count += 1
            
    return count


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