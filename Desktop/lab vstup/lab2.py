text = (input('Enter a text: '))
variant = (input('Choose a variant(A or C): '))

if variant == 'A':
    print('a = ', text.count('a'))
    print('b = ', text.count('b'))
    print('c = ', text.count('c'))
    print('d = ', text.count('d'))
    print('e = ', text.count('e'))
    print('f = ', text.count('f'))
    print('g = ', text.count('g'))
    print('h = ', text.count('h'))
    print('i = ', text.count('i'))
    print('j = ', text.count('j'))
    print('k = ', text.count('k'))
    print('m = ', text.count('m'))
    print('n = ', text.count('n'))
    print('o = ', text.count('o'))
    print('p = ', text.count('p'))
    print('q = ', text.count('q'))
    print('r = ', text.count('r'))
    print('s = ', text.count('s'))
    print('t = ', text.count('t'))
    print('u = ', text.count('u'))
    print('v = ', text.count('v'))
    print('w = ', text.count('w'))
    print('x = ', text.count('x'))
    print('y = ', text.count('y'))
    print('z = ', text.count('z'))



elif variant == 'C':
    my_str = (text)
    words = my_str.split()
    words.sort()
    for word in words:
        print(word)




else:
    print('Програма неверная')