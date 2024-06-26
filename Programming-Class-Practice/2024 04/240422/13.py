# リストの定義
bar = [2, 3, 4, 5, 6]

# リスト内の要素を変更
bar[1] = 20  # インデックス1の要素を20に変更
# bar = [2, 20, 4, 5, 6]

# スライスを使って一部の要素を置き換え
bar[0:3] = [100, 200, 300]  # インデックス0から2までの要素を[100, 200, 300]で置き換え
# bar = [100, 200, 300, 5, 6]

# リストの内容を表示
print(bar)  # 出力: [100, 200, 300, 5, 6]

# リストを新しい値で上書き
bar = [100, 200, 300, 400, 500, 600, 700]

# リストの一部の要素を削除
bar = [10, 20, 30, 40, 50, 60]  # 新しいリストを作成

print("before: ", bar , len(bar))  # 変更前のリストを表示
# 出力: before: [10, 20, 30, 40, 50, 60]

del bar[1]  # インデックス1の要素を削除
# bar = [10, 30, 40, 50, 60]

print("after: ", bar , len(bar))  # 変更後のリストを表示
# 出力: after: [10, 30, 40, 50, 60]
 
bar.remove(50)
print("after: ", bar , len(bar))  

print(bar.pop(2))
print("after: ", bar , len(bar))  