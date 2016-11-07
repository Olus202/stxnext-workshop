def dir_function(obj):
    for attr in dir(obj):
        if callable(attr):
            print(attr)

print(dir_function(123))
