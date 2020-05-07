
import random
import numpy as np


# ListManager class
class ListManager:
    __dataList = []
    __compareCount = 0
    __exchangeCount = 0

    def __init__(self):
        # 100のデータ要素が入るlist
        self.dataList = [0] * 100
        # 配列の長さ分0-10000までのランダムな数字を追加していく
        for i in range(len(self.dataList)):
            self.dataList[i] = random.randint(0, 10000)

    # 2つのデータを比較する
    # np.signでjavaのsignumと同じことができる
    def compare(self, index1: int, index2: int) -> int:
        self.compareCount += 1
        return int(np.sign(self.dataList[index1] - self.dataList[index2]))

    # 2つのデータを入れ替える
    def exchange(self, index1: int, index2: int):
        self.exchangeCount += 1
        tmp = self.dataList[index1]
        self.dataList[index1] = self.dataList[index2]
        self.dataList[index2] = tmp

    # ソートが正しく行われたかをチェックする
    def checkResult(self):
        data = self.dataList[0]
        for i in range(1, len(self.dataList)):
            if data > self.dataList[i]:
                raise Exception(
                    f"ソートされていない: [{(i - 1)}]={data}[{i}]={self.dataList[i]}")
            data = self.dataList[i]
        print(f"ソートOK: 比較={self.compareCount}入れ替え={self.exchangeCount}")

    # データのサイズを取得する
    def size(self) -> int:
        return len(self.dataList)
