def foobar(n):

    for count in range(1, n+1):
        
        div3 = True if count % 3 == 0 else False
        div5 = True if count % 5 == 0 else False
        
        if div3: print('foo', end="")
        if div5: print ('bar', end="")
        if not div3 and not div5: print(str(count), end="")
        print()
        
    return

foobar(15)
