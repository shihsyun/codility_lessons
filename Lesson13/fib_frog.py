"""
Task:FibFrog
Count the minimum number of jumps required for a frog to get to the other side of a river.

The Fibonacci sequence is defined using the following recursive formula:

    F(0) = 0
    F(1) = 1
    F(M) = F(M - 1) + F(M - 2) if M >= 2
A small frog wants to get to the other side of a river. The frog is initially located at one bank of the river (position −1) and wants to get to the other bank (position N). The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. Luckily, there are many leaves on the river, and the frog can jump between the leaves, but only in the direction of the bank at position N.

The leaves on the river are represented in an array A consisting of N integers. Consecutive elements of array A represent consecutive positions from 0 to N − 1 on the river. Array A contains only 0s and/or 1s:

0 represents a position without a leaf;
1 represents a position containing a leaf.
The goal is to count the minimum number of jumps in which the frog can get to the other side of the river (from position −1 to position N). The frog can jump between positions −1 and N (the banks of the river) and every position containing a leaf.

For example, consider array A such that:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the minimum number of jumps by which the frog can get to the other side of the river. If the frog cannot reach the other side of the river, the function should return −1.

For example, given:

    A[0] = 0
    A[1] = 0
    A[2] = 0
    A[3] = 1
    A[4] = 1
    A[5] = 0
    A[6] = 1
    A[7] = 0
    A[8] = 0
    A[9] = 0
    A[10] = 0
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/trainingDTGA4J-AU2/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def fibonacci(N):

    fib = [0]* (N+1)
    fib[1] = 1

    for idx in range(2, N+1):
        fib[idx] = fib[idx-2] + fib[idx-1]

    fib = fib[3:]
    fib.sort(reverse = True)
    
    if len(fib) > 10:
        fib = fib[:10]

    return fib


def solution(A):
    # write your code in Python 3.6
    # 先準備好Fib表，接著計算河中有葉子的距離存成river
    # 查表後count步數回傳

    N = len(A)

    if N <= 2: return 1

    fib_table = fibonacci(N)
    count = 0

    A = [0]+A+[1]
    ptr = 0
    river = []
    for idx in range(len(A)):
        if A[idx] == 1:
            river.append(idx - ptr)
            ptr = idx

    tmp = 0
    while river:
        tmp += river[0]
        if tmp in fib_table:
            count += 1
            tmp = 0
        river = river[1:]

    if tmp > 1:
        return -1

    return count

# testcase 1
A = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]
print(solution(A))

# testcase 2
A = []
print(solution(A))

# testcase 3
A = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(solution(A))

# testcase 4
A = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(solution(A))

#testcase 5
A = [1, 1, 1]
print(solution(A))

#testcase 6
A = [1, 0, 0, 0, 0]
print(solution(A))