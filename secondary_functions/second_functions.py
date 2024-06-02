def groupper(iterable, group_lenght=0):
    # groupper('ABCDEFG',3) → ABC DEF G
    iterator = iter(iterable)
    a = ()
    while True:
        a = list(next(iterator, None) for i in range(group_lenght))
        if None in a:
            a = list(a[i] for i in range(group_lenght) if a[i] is not None)
            break
        yield a
    yield a
