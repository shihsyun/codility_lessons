"""
Task:CountNonDivisible
Calculate the number of elements of an array that are not divisors of each element.

You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
For the following elements:

A[0] = 3, the non-divisors are: 2, 6,
A[1] = 1, the non-divisors are: 3, 2, 3, 6,
A[2] = 2, the non-divisors are: 3, 3, 6,
A[3] = 3, the non-divisors are: 2, 6,
A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..2 * N].
Copyright 2009–2019 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

You can check it out the result at https://app.codility.com/demo/results/training9SHP9B-D7J/ .

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

"""

def solution(A):
    # write your code in Python 3.6
    # 任何數除了自己外，1是所有的除數，所以準備一個陣列div，先把每一個元素的1和自己用集合的方式存進去
    # 找出A的最大值，使用質數篩選法，把各元素的除數放進集合陣列div中，若idx是除數則N // idx也是除數，故一次可以找到兩個。
    # 再來A陣列裡的元素有可能會重複出現，所以需要先計算出現的次數存在count集合裡
    # 此時我們已經可以知道A陣列的每個元素的除數集合與各元素重複出現的次數，此時只要遍歷A陣列，
    # 加總計算各元素存在div的所有除數與count中紀錄的出現次數，再用A陣列長度減去上述總和，即可存進result回傳。
    # 複雜度降為O(N * log(N))
    # more detail please check it out at https://www.martinkysel.com/codility-countnondivisible-solution/ .

    div = {}
    for elem in A:
        div[elem] = set([1, elem])

    A_max = max(A)
    idx = 2
    while idx * idx <= A_max:
        elem = idx
        while elem <= A_max:
            if elem in div and not idx in div[elem]:
                div[elem].add(idx)
                div[elem].add(elem // idx)
            elem += idx
        idx += 1

    count = {}
    for elem in A:
        if elem not in count:
            count[elem] = 1
        else:
            count[elem] += 1

    result = [0]*len(A)
    for idx, elem in enumerate(A):
        tmp = 0
        for value in div[elem]:
            tmp += count.get(value, 0)
        
        result[idx] = len(A) - tmp

    return result     


# testcase 1
A = [3, 1, 2, 3, 6]
print(solution(A))

# testcase 1
A = [3, 4]
print(solution(A))
