# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aGXBrosAlUYH3g2JSEimmSfEqWVFPaGO
"""

#クラスの定義
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人です。")
        else:
            print(f"{self.name}は大人ではありません。")

# インスタンス
humans = [
    Human("太郎", 35),
    Human("一郎", 27),
    Human("二郎", 21),
    Human("三郎", 19),
    Human("四郎", 20),
    Human("五郎", 15),
]

# リストの要素数分だけcheck_adultメソッドを呼び出し
for human in humans:
    human.check_adult()





