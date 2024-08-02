# 条件判定対象の数値を変数varに代入
var = 2   # ここに任意の正の整数を設定

# if文で条件分岐を行い、結果を出力
if var % 3 == 0 and var % 5 == 0:
    print("FizzBuzz")
elif var % 3 == 0:
    print("Fizz")
elif var % 5 == 0:
    print("Buzz")
else:
    print(var)



