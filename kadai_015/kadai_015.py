### 課題015
### 15章で学んだ知識を活かして、Humanクラスを定義し、名前と年齢を出力するプログラムを作ります。

# 名前(name)と年齢(age)の属性を持つHumanクラスを作成してください。
# nameとageを標準出力(print)するメソッド(printinfo)を追加してください。
# Humanクラスのインスタンスは、変数に代入してプログラム内で使用してください。


class Human:
   # コンストラクタを定義する
   def __init__(self, name, age):
     self.name = name
     self.age = age

   # メソッドを定義する
   def set_name(self, name):
     self.name = name

   def printinfo(self):
     print(self.name)


# インスタンス化する
human = Human("侍小太郎", 29)

# 属性にアクセスし、値を出力する
print(human.name)
print(human.age)

# End
