def quicksort(array):
  if len(array) < 2:
    # base case, arrays with 0 or 1 element are already "sorted"
    return array
  else:
    # 再帰処理開始
    pivot = array[0]
    # ピボットを基点に、array[0]以下の数値の列を作成する
    less = [i for i in array[1:] if i <= pivot]
    # ピボットを基点に、array[0]より大きい数値の列を作成する
    greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

print(quicksort([20, 15, 10, 5, 2, 3])) # [2, 3, 5, 10, 15, 20]

