def field(dicts: list[dict], *args) -> iter:
    """Создает генератор для отбора записей в списке словарей
    items по ключам, указанным в args."""
    assert len(args) > 0
    if len(args) == 1:
        for d in dicts:
            if args[0] in d and d[args[0]] is not None:
                yield d[args[0]]
    else:
        for d in dicts:
            temp_dict = {}
            for key in args:
                if key in d and d[key] is not None:
                    temp_dict[key] = d[key]

            if temp_dict:
                yield temp_dict


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print(str(list(field(goods, 'title')))[1:-1])
    print(str(list(field(goods, 'title', 'price')))[1:-1])
