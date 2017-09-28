def repeat_func(num, func, result_list):
    if num >= 1:
        result_list.append(func(num))
        return repeat_func(num-1, func, result_list)
    else:
        pass

def fibonacci(n, a=1, b=0):
    return b if n < 1 else fibonacci(n-1, a+b, a)

def fib2(n):
    if n<=1:
        return n
    result = [1,0,0,1]
    matrix = [1,1,1,0]
    while n>0:
        if n%2:
            result=mul(matrix, result)
        matrix=mul(matrix, matrix)
        n //= 2
    return result[2]
def mul(a, b):
    return [a[0]*b[0] + a[1]*b[2],
            a[0]*b[1] + a[1]*b[3],
            a[2]*b[0] + a[3]*b[2],
            a[2]*b[1] + a[3]*b[3]]

'''
sequens_list = []
repeat_func(979612319, fibonacci, sequens_list)
print(sequens_list)

sequens_list.reverse()
print(sequens_list)
'''
#print(fib2(979612319))
print(fib2(97))