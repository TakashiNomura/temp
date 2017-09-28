def repeat_func(num, func, result_list):
    if num >= 1:
        result_list.append(func(num))
        return repeat_func(num-1, func, result_list)
    else:
        pass

def fibonacci(n, a=1, b=0):
    return b if n < 1 else fibonacci(n-1, a+b, a)

def fibo(n):
    a1, a2 = 1, 0
    while n > 0:
        a1, a2 = a1 + a2, a1
        n -= 1
    return a1
'''
sequens_list = []
repeat_func(101, fibonacci, sequens_list)

print(sequens_list)

sequens_list.reverse()
print(sequens_list)
'''
f = fibo(655365569)
print(f)
