# def solution(A):
#     # write your code in Python 3.6
#     undup_A = list(set(A))
#     undup_A.sort()
#     filterd_A = [a for a in undup_A if a >= 0]
#
#     return_value = 1
#     counter = 1
#     for v in filterd_A:
#         if v == counter:
#             counter += 1
#             continue
#         return_value = counter
#         break
#     if counter == len(filterd_A) + 1:
#         return_value = counter
#     return return_value
#
#
# # l = [1, 3, 6, 4, 1, 2]
# # l = [1, 2, 3]

"""
list A 空じゃない
N個の要素
数値 0 <= K <= N - 1
Aを二つに分ける
left  ; A[0], A[1] ~ A[K]
right : A[K+1], A[K+2] ~ A[N-1]

左と右の最大値の絶対的な差が最大化すKを見つけろ


"""

# def solution(A):
#
#     max_abs_diff = 0
#     len_a = len(A)
#     for i in range(len_a):
#         if i == len_a - 1:
#             break
#         abs_diff = abs(max(A[:i+1], key=abs) - max(A[i+1:], key=abs))
#         if abs_diff > max_abs_diff:
#             max_abs_diff = abs_diff
#     return max_abs_diff
#
# array = [1, 3, -3]
# re = solution(array)
# print(re)


"""
連続したN日の自由な休み
Location No: 0 から N -1
0 <= K < N
K日目の場所A[K]
Key: 日目、Value：場所
1回の旅行で複数の場所を提案される

毎日旅行したい、できれば全部の場所に行きたい。
同じ場所に2回以上訪れても良いが、同じ訪問先は最小回数でなければならない。
連続した休みの範囲で全てを訪れつつ、最も短い休暇日数を見つけること。

"""


def solution(A):
    mandatory_set = set(A)
    len_A = len(A)
    len_all_elements = len(mandatory_set)
    min_days = len_A
    for i in range(len_A):
        trip_locs = set()
        start_k, end_k = i, len_A
        for inner_i in range(start_k, len_A):
            trip_locs.add(A[inner_i])
            if set(trip_locs) == mandatory_set:
                end_k = inner_i
                break
        if trip_locs != mandatory_set:
            continue
        days = end_k - start_k + 1
        if days < min_days:
            min_days = days
            if days == len_all_elements:
                break
    return min_days

array = [7, 3, 7, 3, 1, 3, 4, 1]
re = solution(array)
print(re)
