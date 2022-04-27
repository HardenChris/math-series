def fibonacci(n):   
    if n == 0: 
        return 0
    elif n == 1 or n == 2: 
        return 1
    else:
        return n * fibonacci((n - 1 ) + (n - 2))

def lucas(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return n * lucas((n - 1) + (n - 2))


def sum_series(n, f_num=0, s_num=1):
    if f_num == 0 and s_num == 1:
        return fibonacci(n)
    elif f_num == 2 and s_num == 1:
        return lucas(n)











'''
    def w_series(n, start_num=0, second_num=1):
        print (n, start_num, second_num) 

    w_series(3,2)
'''
