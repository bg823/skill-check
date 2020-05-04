"""
Q005 データクラスと様々な集計
以下のファイルを読み込んで、WorkDataクラスのインスタンスを作成してください。
resources/q005/data.txt
(先頭行はタイトルなので読み取りをスキップする)
読み込んだデータを以下で集計して出力してください。
(1cccdccvsvvfvfvf 役職別の合計作業時間
(2) Pコード別の合計作業時間
(3) 社員番号別の合計作業時間
上記項目内での出力順は問いません。

作業時間は "xx時間xx分" の形式にしてください。
また、WorkDataクラスは自由に修正してください。

[出力イメージ]
部長: xx時間xx分
課長: xx時間xx分
一般: xx時間xx分
Z-7-31100: xx時間xx分
I-7-31100: xx時間xx分
T-7-30002: xx時間xx分
（省略）
194033: xx時間xx分
195052: xx時間xx分
195066: xx時間xx分
（省略）
"""

import pandas as pd
from WorkData import WorkData


def read_file():
    try:
        corp_data = pd.read_csv('data2.txt')
        return corp_data
    except OSError as err:
        print("can't open file and readlines{0}".format(err))


if __name__ == "__main__":
    corp_data = read_file()
    # create instance
    work_data = WorkData()
    # 役職別時間
    work_data.worker_time_format(work_data.worker_position(corp_data))
    # P-CODE別時間
    work_data.worker_time_format(work_data.worker_pCode(corp_data))
    # 社員番号別時間
    work_data.worker_time_format(work_data.worker_num(corp_data))
    # 部署別時間
    # work_data.worker_time_format(work_data.worker_department(corp_data))

# 完成までの時間: 30分
