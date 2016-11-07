def dir_with_doc(obj):
    for attr in dir(obj):
        print(attr)
        print(attr.__doc__)
        print("-" * 20)

dir_with_doc(123)
