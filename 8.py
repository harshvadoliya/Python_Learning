for i in range(5):
    print('  '*i, end='')
    for j in range(1, 6 - i):
        print( j*2, end=' ')
    print()