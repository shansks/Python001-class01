def map(func,args):
    result = []
    for i in args:
        result.append(func(i))
    return result