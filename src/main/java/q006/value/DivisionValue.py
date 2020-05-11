"""
割り算を行うクラス
"""

from IValue import IValue
from operator import *


# IValueを実装する
class DivisionValue(IValue):
    def execute(self, values):
        right = values.pop()
        left = values.pop()
        # 割り算
        values.append(truediv(right, left))
