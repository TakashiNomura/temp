# TODO フィボナッチ数列を求めるプログラムを元に修正する

import sys

# 部屋数を返す
def getroomnum(a):
    if a < 3:
        return 1
    elif a >= 3 and a < 16:
        b = getroomnum(a-1) + getroomnum(a-2)
        return b
    elif a >= 16:
        c = getroomnum(a-1) + getroomnum(a-2)
        return c % 16

lines = sys.stdin.readlines()
for i, line in enumerate(lines):
    line = line.strip("\n")
    if line.isdigit() == True:
        floor = int(line)
        room = getroomnum(floor)
        print(room)

