### 課題017
### この教材で学んだ知識を活かして、Humanインスタンスが成人かどうかチェックするプログラムを作ります。

# 名前(name)と年齢(age)の属性を持つHumanクラスを作成してください。
# Humanクラスには、以下の条件で標準出力(print)するcheck_adultメソッドを追加してください。
#     ageが20以上の場合に大人であること
#     そうでない場合に大人でないこと

# Humanクラスのインスタンスを複数生成してリストに追加し、リストの要素数分だけcheck_adultメソッドを呼び出してください。
# 名前(name)と年齢(age)の属性を持つHumanクラスを作成してください。

class Human:
   # コンストラクタを定義する
   def __init__(self, name, age):
     self.name = name
     self.age = age

   # メソッドを定義する
   def set_name(self, name):
     self.name = name

   def check_adult(self):
     if self.age >= 20:
       print(f"{self.name} さんは{self.age}歳なので、大人です")
     else:
       print(f"{self.name} さんは{self.age}歳なので、大人ではないす")
     

# 年齢リスト
list_age = {"次郎":20, "花子":19, "一郎":25, "桃子":9, "友蔵":60}


# 処理メイン
for k in list_age.keys():
  # インスタンス化する
  human = Human(k, list_age[k])

  # check_adultメソッド
  human.check_adult()


# End
