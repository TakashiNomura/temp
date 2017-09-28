# coding: UTF-8
import sys

# フィボナッチ数を返す
def fibonacci(n):
    a1, a2 = 1, 0
    while n > 0:
        a1, a2 = a1 + a2, a1
        n -= 1
    return a1

lines = sys.stdin.readlines()
for i, line in enumerate(lines):
    line = line.strip("\n")
    if line.isdigit() == True:
        floor = int(line)
        room = fibonacci(floor)
        if floor < 16:
            print(room)
        if floor >= 16:
            print(room%16)
