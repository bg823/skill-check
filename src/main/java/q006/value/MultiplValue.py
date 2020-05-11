"""
掛け算を行うクラス
"""

from IValue import IValue
from operator import *


# IValueを実装する
class MultiplValue(IValue):
    def execute(self, values):
        right = values.pop()
        left = values.pop()
        # 掛け算
        values.append(mul(right, left))
