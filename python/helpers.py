def memo(f):
    mem = {}
    def inner(*args):
        arg_string = '-'.join([f'{i},{arg}' for i, arg in enumerate(args)])
        key = f'{__file__}-{f.__name__}-{arg_string}'
        if key not in mem:
            mem[key] = f(*args)
        return mem[key]
    return inner
