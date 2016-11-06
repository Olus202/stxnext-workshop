def filter_function(*args):
    words = list(filter(lambda x: len(x) > 4, args))
    return words

print(filter_function("ola", "matylda"))
