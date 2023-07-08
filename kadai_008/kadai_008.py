### 課題008
### 8章で学んだ知識を活かして、FizzBuzz問題のプログラムを作ります。

# 変数varが3の倍数の場合はFizz、5の倍数の場合はBuzz、3と5の倍数の場合はFizzBuzz、それ以外の場合は変数varを出力する条件式を記述してください。
# ただし、変数varは正の整数とします。



#ランダムな整数を利用するために、randomモジュールをインポート
import random

# 変数varに0-100までのランダムな整数を代入する
var = random.randint(0, 100)

# まず変数varの値を出力
# print(var)

# 変数varが3と5の倍数の場合はFizzBuzzを出力
if var % 3 == 0 and var % 5 == 0:
    print(f"{var} FizzBuzz")
    
# 変数var5の倍数の場合はBuzzを出力
elif var % 5 == 0:
    print(f"{var} Buzz")
    
# 変数varが3倍数の場合はFizzを出力
elif var % 3 == 0:
    print(f"{var} Fizz")
    
# それ以外の場合は変数varを出力
else:
    print(var)

# End of Source
