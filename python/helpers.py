def memo(f):
    mem = {}
    def inner(*args, **kwargs):
        arg_string = '-'.join([f'{i},{arg}' for i, arg in enumerate(args)])
        kwarg_string = '-'.join([f'{key}:{val}' for key, val in kwargs.items()])
        key = f'{__file__}-{f.__name__}-{arg_string}-{kwarg_string}'
        if key not in mem:
            mem[key] = f(*args, **kwargs)
        return mem[key]
    return inner
