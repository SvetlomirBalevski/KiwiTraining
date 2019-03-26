def f_c(X):
    """
        The function return 4, doesn't matter how it
        it is used
    """
    return 4


def f_x(x, a, b):
    """
    :return: f(x) = a*x + b
    """
    try:
        return x * a + b
    except TypeError:
        print("Number should be used, not string")
        exit()

def sum(x):
    """
    :return: the sum of f_x() called
    3 times with parameters x, 1, 1, x, 2, 2, x, 3, 3
    """
    return f_x(x,1,1) + f_x(x,2,2) + f_x(x,3,3)

#Tests
#if __name__ == '__main__':
#    print(f_c(232))
#    print(f_x(1,2,4))
#    print(sum(2))