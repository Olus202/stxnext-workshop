def dir_function(obj):
    for attr in dir(obj):
        print(attr)

print(dir_function(111))
