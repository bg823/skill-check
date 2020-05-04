

"""
方法として考えているのが辞書型にして、keyは重複を無くしてvalueをまとめる
list化したnumberとworkTimeを結合

number => sum worktime
"""
from collections import defaultdict
import pandas as pd
import numpy as np


# 一行目読まない感じであれば、先頭にラベルをつけて集計
class WorkData:

    number = ''  # 社員番号
    department = ''  # 部署
    position = ''  # 役職
    pCode = ''  # pCode
    workTime = 0  # 作業時間

    # 社員番号で作業時間をまとめる
    def worker_num(self, data_list) -> dict:
        worker_number = pd.pivot_table(
            data_list, index='社員番号', columns=None, values='作業時間', aggfunc=np.sum)
        # 辞書型にしてフォーマット関数へ
        wnum_time = worker_number.to_dict()
        return wnum_time

    # 部署で作業時間をまとめる
    def worker_department(self, data_list) -> dict:
        worker_department = pd.pivot_table(
            data_list, index='部署名', columns=None, values='作業時間', aggfunc=np.sum)
        wdep_time = worker_department.to_dict()
        return wdep_time

    # 役職で作業時間をまとめる
    def worker_position(self, data_list) -> dict:
        worker_position = pd.pivot_table(
            data_list, index='役職名', columns=None, values='作業時間', aggfunc=np.sum)
        wposi_time = worker_position.to_dict()
        return wposi_time

    # P-CODEで作業時間をまとめる
    def worker_pCode(self, data_list) -> dict:
        wordker_pCode = pd.pivot_table(
            data_list, index='P-CODE', columns=None, values='作業時間', aggfunc=np.sum)
        wpcode_time = wordker_pCode.to_dict()
        return wpcode_time

    # time format
    def worker_time_format(self, data_sum: dict):
        for keys, values in data_sum.items():
            for key, value in values.items():
                print(f"{key}: {value // 60}時間{value % 60}分")
