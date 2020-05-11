"""
足し算を行うクラス
"""

from IValue import IValue
from operator import *


# IValueを実装する
class PlusValue(IValue):

    def execute(self, values):
        right = values.pop()
        left = values.pop()
        # 足し算
        values.append(add(right, left))
