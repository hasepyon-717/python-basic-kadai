### 課題013
### Pythonで関数を使ったプログラムが書けるようになること。

# 商品を購入して、消費税を加えた計算結果を返す関数を記述してください。
# 第1引数に商品の金額、第2引数に消費税（10%）を設定できるようにしてください。
# 計算結果で小数点が含まれる場合はそのまま表示してください。
# 切り捨てや四捨五入などの処理は不要です。


# 消費税を算出する関数
def calculate_total(price, sales_tax):
 # 商品代金に消費税分を加える
 total = price * (1 + sales_tax / 100)

 # 変数totalの値を出力する
 print(f"{total}円")


# 関数コール、引数に商品の金額、消費税（10%）を渡す
calculate_total(1000, 10)


# End
