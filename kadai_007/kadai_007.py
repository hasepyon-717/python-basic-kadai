### 課題007
### リストとディクショナリから水曜日の天気予報を取り出すプログラム



list = [
"月曜日は晴れです",
"火曜日は雨です",
"水曜日は晴れです",
"木曜日は晴れです",
"金曜日は曇りです",
"土曜日は曇りのち雨です",
"日曜日は雷雨です"]


dictionary = {
"mon":"晴れ",
"tue":"雨",
"wed":"晴れ",
"thu":"晴れ",
"fri":"曇り",
"sat":"曇りのち雨",
"sun":"雷雨",
}

# listからの表示
print(list[2])

# Dictionaryからの表示
print(f'水曜日は {dictionary["wed"]} です')