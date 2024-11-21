def oxford_comma(items):
    if len(items) == 2:
        return ' and '.join(items)
    elif len(items) > 2:
        prev_items = ', '.join(items[:-1])
        return prev_items + ', and ' + items[-1]
    else:
        return items[0]

