"""
Q006 空気を読んで改修

標準入力から「逆ポーランド記法」で記載された1行の入力を受け取り、その計算結果を出力する処理を実装してください。
実装するのは四則演算（+ - * /）です。

https://ja.wikipedia.org/wiki/%E9%80%86%E3%83%9D%E3%83%BC%E3%83%A9%E3%83%B3%E3%83%89%E8%A8%98%E6%B3%95

ただし、現状は以下の実装が終わっています。
- 逆ポーランド記法を分解して、計算しやすい値リストに変換する処理の一部（Q006.parseLine）
- 計算しやすい値として管理するためのクラス群の一部（IValue,DecimalValue,PlusValue）

途中まで終わっている実装を上手く流用しながら、残りの処理を実装してください。
エラー入力のチェックは不要です。
実行例：
入力） 3 1.1 0.9 + 2.0 * -
出力） -1
（または -1.00 など、小数点に0がついてもよい）

"""
from PlusValue import PlusValue as pv
from SubValue import SubValue as sv
from MultiplValue import MultiplValue as mv
from DivisionValue import DivisionValue as dv
from DecimalValue import DecimalValue as decv

from IValue import*


class Q006:
    def _parseLine(self, lineText: str) -> list:
        resultList = []
        # pythonにはswitchがないため、if文で記述
        for text in lineText.split():
            if text == "+":  # 足し算
                resultList.append(pv())
            elif text == "-":  # 引き算
                resultList.append(sv())
            elif text == "*":  # 掛け算
                resultList.append(mv())
            elif text == "/":  # 割り算
                resultList.append(dv())
            else:  # その他は数値として扱う
                resultList.append(decv(text))

        return resultList


if __name__ == "__main__":
    lineText = input()
    q6 = Q006()
    line = q6._parseLine(lineText)

    print(line)
# 完成までの時間: 1時間 15分
