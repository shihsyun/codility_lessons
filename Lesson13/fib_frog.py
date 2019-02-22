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

You can check it out the result at https://app.codility.com/demo/results/trainingKFWXX3-YVC/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(A):
    # write your code in Python 3.6
    # 這題需要使用Dynamic programming演算法解決，DP的說明可以參考這個
    # http://www.csie.ntnu.edu.tw/~u91029/DynamicProgramming.html
    # 先將A append 1代表另一岸並預先準備小於N的fib表，先設長度為27，再去除[0, 1]與大於Ｎ之後的部份
    # 準備好next_try陣列，並將fib表中的位址-1處都先標記為1，代表青蛙第一次就可以跳到這些地方(因為青蛙是從-1開始跳)
    # 接著依序檢查next_try[idx] > 0(代表這個位址青蛙可以跳到)與A[idx]是否等於1(代表有葉子)
    # 開始依序檢查idx+fib是否超過N　有則需要break 跳到下一個位置 如果沒有再接著判斷
    # next_try的[idx+fib]是否<0  這代表青蛙還沒來過
    # 或next_try[idx+fib] > next[idx]+1 這代表idx+fib是比idx+1更好的選擇
    # 如果以上兩者其一成立，將next[idx]+1放入next_try[idx+fib]中，跑完迴圈後回傳next_try[-1]就是最少步數
    # 複雜度降為O(N*log(N))
    # more detail please check it out at https://www.martinkysel.com/codility-fibfrog-solution/#comment-4291808529 .

    A.append(1)
    N = len(A)

    fib_table = [0]*27
    fib_table[1] = 1

    for idx in range(2, 27):
        fib_table[idx] = fib_table[idx-1] + fib_table[idx-2]
        if fib_table[idx] > N:
            break
    
    fib_table = fib_table[2:idx]

    next_try = [-1]*N
    for idx in range(len(fib_table)):
        next_try[fib_table[idx] - 1] = 1

    for idx, leaf in enumerate(A):
        if next_try[idx] > 0 and leaf == 1:
            for fib in fib_table:
                if idx + fib >= N:
                    break
                if next_try[idx+fib] < 0 or next_try[idx+fib] > next_try[idx]+1:
                    next_try[idx+fib] = next_try[idx]+1

    return next_try[-1]

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