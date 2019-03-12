def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(10))

"""

如果我们计算fact(5)，可以根据函数定义看到计算过程如下：

===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120

"""
print(fact(5))

# 利用递归函数移动汉诺塔:

def move(n, a, b, c):

    if n == 1:

        print('move', a, '-->', c)

    else:

        move(n-1, a, c, b)

        move(1, a, b, c)

        move(n-1, b, a, c)



move(4, 'A', 'B', 'C')