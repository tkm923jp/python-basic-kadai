# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1aGXBrosAlUYH3g2JSEimmSfEqWVFPaGO
"""

class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def set_name(self, name):
    self.name = name
  def set_age(self, age):
    self.age = age

  def printinfo(self):
    print( self.name)
    print( self.age)

human = Human("太郎", 35)

human.printinfo()



