"""
Output
I=3
a=5
about=2
against=1
all=1
although=1
always=2
backward=1
balance=1
begins=1
behind=1
bicycle=1
but=3
can=5
cannot=2
clouds=1
come=1
communication=1
conquer=1
courage=1
created=1
creating=1
darkness=2
dead-end=1
depends=1
detour=1
didn’t=1
do=5
doing=1
dream=1
dreams=1
drive=2
every=1
everyday=1
experience=1
fail=1
failing=1
failure=1
fear=1
finding=1
from=1
full=2
future=1
glory=1
great=1
greatest=1
growth=1
happens=2
happiness=1
haste=1
hate=2
have=1
hearing=1
highest=1
if=2
ignorance=1
important=1
in=3
increasing=1
is=14
isn't=1
isn’t=1 カンマの違い...
it=6
its=1
keep=2
kindness=1
kites=1
life=6
light=2
like=1
love=3
me=1
more=1
most=1
moving=1
must=1
my=3
never=2
not=5
of=3
often=1
one=1
only=2
our=1
ourselves=1
out=2
overcoming=1
painful=1
peace=1
please=1
process=1
pursue=1
rather=1
religion=1
rest=1
riding=1
rise=1
rising=1
said=1
scares=1
slowly=1
small=1
smile=1
so=1
speed=1
springs=1
starts=1
street=1
suffering=1
than=2
that=3
the=8
them=1
there=2
thing=2
things=1
time=1
to=5
today=1
tomorrow=1
true=2
up=1
upon=1
walk=2
we=1
what=4
wind=1
with=4
without=2
world=2
you=8
your=2
yourself=3
"""


from collections import Counter
import sys


# 名言を整形する(format famous quotes)
def format_famous_quotes(famous_quotes: list) -> list:
    formated_phrase = []

    for phrase in famous_quotes:
        # 単語以外の不要な物は削除する(maketrans and translate are used in pairs)
        subphrase = phrase.maketrans({',': '', ';': '', '.': '', '–': ''})
        add_line = phrase.translate(subphrase)

        # new_linesのリストに値を追加していく(add new_lines)
        formated_phrase.append(add_line)

    return famous_quotes_to_word(formated_phrase)


# phraseを単語ごとに区切って、I以外の単語は全て小文字に変換する
def famous_quotes_to_word(formated_phrase: list) -> list:
    counter_word = []
    for words in formated_phrase:
        # 空白で分割(split on white space)
        word = words.split()
        # 大文字のI以外は小文字に変換してlistに追加
        for reword in word:
            if reword == 'I':
                counter_word.append(reword)
            else:
                counter_word.append(reword.lower())

    return out_put_format(counter_word)


# 出力用フォーマットと出力
def out_put_format(counter_word: list) -> bool:
    # 単語の数数える(counting word)
    counted = Counter(counter_word)
    # 単語順で、ソートするして出力(sorted word and output)
    # ソートしたあとはタプル型なのでインデックス指定
    for out_put in sorted(counted.items()):
        print(f"{out_put[0]}={out_put[1]}")

    return True


# 実行
if __name__ == "__main__":
    try:
        # file open
        famous_quotes = open('data.txt')
        # 各行をlinesに格納
        lines = famous_quotes.readlines()
    except OSError as err:
        print("can't open file and readlines{0}".format(err))

    format_famous_quotes(lines)
    famous_quotes.close()

# 完成までの時間: 23分
