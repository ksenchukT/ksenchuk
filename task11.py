def na3(n):
    if n%3 == 0 and n%5 == 0:
        print('Foobar')
    elif n%5 == 0:
        print ('Bar')
    elif n%3 == 0 :
        print('Foo')

na3(9)
na3(25)
na3(15)