"""
Task:MaxCounters
Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.

You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/training8XRQEK-GD6/ .
"""

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N ,A):
    
    # write your code in Python 3.6
    # 使用lazy-write去處理performance issue，複雜度降為O(N + M)
    # 需要兩個變數分別去紀錄
    # 1. 截至目前為止須切齊的最大值，並在主迴圈與回傳檢查迴圈中做Ｘ的陣列元素替換
    # 2. 計算在１<=X<=N情形下的操作最大值，並在>N的情形下，將須切齊的最大值替換成操作最大值
    # more detial please check it out at https://codesays.com/2014/solution-to-max-counters-by-codility/#comment-445 .

    result = [0]*N
    max_to_set = 0
    current_max = 0
    for idx in A:
        if 1 <= idx <= N:
            
            if result[idx-1] < max_to_set:
                result[idx-1] = max_to_set

            result[idx-1] += 1

            if current_max < result[idx-1]:
                current_max = result[idx-1]

        else:
            max_to_set = current_max

    result = [max(max_to_set, i) for i in result]
    return result


N = 5
A = [3 ,4 ,4 ,6 ,1, 4, 4]
print(solution(N , A))