import bisect
print('████████████████ S T A R T ████████████████')


def linear_search(value, searched_list):
    """ 線形探索 計算量 O(n)
    配列などに格納されたデータ列の先頭から末尾まで順番に、
    探しているデータと一致するか比較していく手法。"""
    print("線形探索-----------")
    for i, num in enumerate(searched_list):
        if value == num:
            print(f"{value}は{i}番目")
            break
        else:
            print(f"{value}なし")


# # 検索対象リスト
# input_list = [3, 5, 9, 12, 15, 21, 29, 35, 42, 51, 62, 78, 81, 87, 92, 93]
# # 検索したい要素
# key = 62
# linear_search(key, input_list)


def binary_search(value, searched_list):
    """ 二分探索 計算量は O(log n) """
    print("二分探索-----------")
    left = 0  # 探索する範囲の左端を設定
    right = len(searched_list) - 1  # 探索する範囲の右端を設定
    while left <= right:
        mid = (left + right) // 2  # 探索する範囲の中央を計算
        if searched_list[mid] == value:
            # 中央の値と一致した場合は位置を返す
            print(mid)
            print(f"{value}は{mid}番目")
        elif searched_list[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
    print(f"{value}なし")


def bubble_sort(arr):
    """バブルソート
    横同士の大小を比較交換をし、更にそれを変更の必要がなくなるまで行う。シンプルでわかりやすい。
    """
    change = True
    while change:
        change = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                change = True
    return arr


def select_sort(arr):
    """選択ソート
    配列中の最小か最大を選択し、それを端に移動させていく。
    """
    for ind, ele in enumerate(arr):
        min_ind = min(range(ind, len(arr)), key=arr.__getitem__)
        arr[ind], arr[min_ind] = arr[min_ind], ele
    return arr


def insert_sort(arr):
    """挿入ソート
    左から順に、整列してある配列の適当な部分に挿入していく。
    挿入する場所を探す際、2分探索を用いることで高速化出来る。
    マージソートやクイックソートに比べ、データの状態に依存しない。
    ほとんどソート済みの配列や、比較的小さな配列に対して強い。
    """
    # 二分探索を用いない場合
    for i in range(1, len(arr)):
        j = i - 1
        ele = arr[i]
        while arr[j] > ele and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = ele
    return arr


def insert_sort_bin_builtin(arr):
    """二分探索用モジュールを使った挿入ソート"""
    for i in range(1, len(arr)):
        bisect.insort(arr, arr.pop(i), 0, i)
    return arr


def merge_sort(arr):
    """マージソート
    最初に分割を繰り返し、その後順に結合していく。結果としては、分割と結合が再帰的に行われる。
    結合する過程でソートされていく。ソートされた配列同士の結合のため、結合の仕方を工夫する。
    結合にheapqのmergeを用いることも出来る。ある程度まで分割できたら、別のソートアルゴリズムを用いることで高速化出来る。
    かなり早いがメモリを多く使う。並列で処理が可能
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    # ここで分割を行う
    left = arr[:mid]
    right = arr[mid:]

    # 再帰的に分割を行う
    left = merge_sort(left)
    right = merge_sort(right)

    # returnが返ってきたら、結合を行い、結合したものを次に渡す
    return merge(left, right)


def merge(left, right):
    merged = []
    l_i, r_i = 0, 0

    # ソート済み配列をマージするため、それぞれ左から見ていくだけで良い
    while l_i < len(left) and r_i < len(right):
        # ここで=をつけることで安定性を保っている
        if left[l_i] <= right[r_i]:
            merged.append(left[l_i])
            l_i += 1
        else:
            merged.append(right[r_i])
            r_i += 1

    # 上のwhile文のどちらかがFalseになった場合終了するため、あまりをextendする
    if l_i < len(left):
        merged.extend(left[l_i:])
    if r_i < len(right):
        merged.extend(right[r_i:])
    return merged


def quick_sort(arr):
    """クイックソート
    基準値を決めて、その基準値から見て大小の2つの配列に分ける。
    この基準値の選び方として、配列の最初や最後、適当な3つぐらいの値の中央値などを用いる。
    分けたグループの中で、更に再帰的に同じ処理を行っていく。基準値の決め方に性能が左右される。
    ある程度まで分割できたら、別のソートアルゴリズムを用いることで高速化出来る。
    かなり早いがメモリを多く使う。安定なソートではない。
    """
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    # データの状態に左右されないためにrandom.choice()を用いることもある。
    # ref = random.choice(arr)
    ref = arr[0]
    ref_count = 0

    for element in arr:
        if element < ref:
            left.append(element)
        elif element > ref:
            right.append(element)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right


def count_sort(arr):
    """カウントソート
    それぞれの値の個数を数えていく。実装が簡単。値の範囲によってはかなり高速。
    """
    max_num = max(arr)
    min_num = min(arr)
    count = [0] * (max_num - min_num + 1)
    for ele in arr:
        count[ele - min_num] += 1

    return [ele for ele, cnt in enumerate(count, start=min_num) for __ in range(cnt)]


# input_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(binary_search(90, input_list))

arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(count_sort(arr))

print('██████████████████ E N D ██████████████████')
