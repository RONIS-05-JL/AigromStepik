from aiogram.types import KeyboardButton


def groupper(iterable: iter, group_lenght: int = 1)-> list[list[KeyboardButton]]:
    '''Сортировка итерируемого объекта в группы '''
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


def buttomer(iterable: iter) -> list[KeyboardButton]:
    ''' Функуия для преобразования списка в кнопки для клавиатуры '''
    return [KeyboardButton(text=f'{iterable[i]}') for i in range(len(iterable))]
