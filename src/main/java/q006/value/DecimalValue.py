"""
数値を保持するクラス
"""

from IValue import IValue
from decimal import*


class DecimalValue(IValue):
    # 保持する値
    _value = None

    def __init__(self, text: str):
        self._value = Decimal(text)
        pass

    def execute(self, values):
        # スタックに値を積む
        values.append(self._value)
