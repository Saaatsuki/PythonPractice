#　性別を入力してもらう
性別 = input("あなたの性別は何ですか？：")

#もし男ならMAN、もし女ならWOMAN。それ以外ならエラーメッセージですと出力

if (性別 == "男"):
    print("MAN")
elif (性別 == "女"):
    print("WOMAN")
else:
    print("エラーメッセージです☆")