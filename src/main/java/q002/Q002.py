"""
Output

1,伊藤
2,井上
3,加藤
4,木村
5,小林
6,斉藤
7,佐々木
8,佐藤
9,清水
10,鈴木
11,高橋
12,田中
13,中村
14,林
15,松本
16,山口
17,山田
18,山本
19,吉田
20,渡辺
"""


# フォーマットメンバーリスト(format member list)
def format_list(members: list) -> dict:
    member = []
    for mem in members:
        # カンマで区切ってlist作成(Create a list by dividing with commas)
        member.append(mem.split(','))

        # 辞書型で、次のフォーマットへ
    return conv_int(dict(member))


# int型に変換して、再度辞書に追加
def conv_int(member: dict) -> dict:
    conv_member = {}
    # キーをintに変換して、新しい辞書に追加(Convert key to int and add to new dictionary)
    for conv_key, conv_val in member.items():
        conv_key = int(conv_key)
        conv_member[conv_key] = conv_val

    return out_put_format(conv_member)


# 出力用フォーマット(sorted values)
def out_put_format(conv_member: dict) -> bool:
    for line_up in sorted(conv_member.items()):
        print(f"{line_up[0]},{line_up[1]}")

    return True


# 実行
if __name__ == "__main__":
    # input
    member_list = ["8,佐藤", "10,鈴木", "11,高橋", "12,田中", "20,渡辺",
                   "1,伊藤", "18,山本", "13,中村", "5,小林", "3,加藤",
                   "19,吉田", "17,山田", "7,佐々木", "16,山口", "6,斉藤",
                   "15,松本", "2,井上", "4,木村", "14,林", "9,清水"
                   ]

    format_list(member_list)


# 完成までの時間: 10分
