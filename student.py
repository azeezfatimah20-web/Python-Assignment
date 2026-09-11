print('import module..')


test = 'testing module'


def findIndex(searchIn, target):
    for i, value in enumerate(searchIn):
        if value == target:
            return i
        return f'Not Found{-1}'
