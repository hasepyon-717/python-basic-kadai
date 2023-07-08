### 課題011
### 11章で学んだ知識を活かして、リストの中身を先頭から全て取り出すプログラムを作ります。

# リストの中身を先頭から全て取り出して、出力結果が以下のようになるプログラムを、for、while、それぞれを利用して記述して下さい。


# 課題リスト
list = ["水","金","地","火","木","土","天","海","冥"]


# for文
print("for文での出力")
for planet in list:
  print(planet)


print("\n\n")


# while文
print("while文での出力")
i=0
while i < len(list):
  print(list[i])
  i=i+1

# End of Source
