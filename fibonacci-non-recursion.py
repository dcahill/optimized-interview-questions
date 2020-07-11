def fibonacci(number):
    a = 0
    b = 1
    for count in range(number):
        if count == 0: print('0')
        elif count == 1: print('1')
        else:
            result = a + b
            print(result)
            a = b
            b = result

fibonacci(12)   
fibonacci(1)
fibonacci(120)
