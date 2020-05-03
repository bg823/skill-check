"""
Q004 ソートアルゴリズム

ListManagerクラスをnewして、小さい順に並び変えた上でcheckResult()を呼び出してください。

実装イメージ:
ListManager data = new ListManager();
# TODO 並び換え
data.checkResult();

- ListManagerクラスを修正してはいけません
- ListManagerクラスの dataList を直接変更してはいけません
- ListManagerクラスの比較 compare と入れ替え exchange を使って実現してください
"""


from ListManager import ListManager


#
def sort(dataList: list):
    for num1 in range(lm.size()):
        for num2 in range(lm.size() - 1):
            if lm.compare(num2, num1) >= 0:
                lm.exchange(num2, num1)
            else:
                continue


if __name__ == "__main__":
    lm = ListManager()

    sort(lm.dataList)

    lm.checkResult()

# 完成までの時間: 79分
