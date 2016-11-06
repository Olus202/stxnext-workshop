import string

def not_in_alphabeth(text):
    result = ""
    for i in text:
        if i in string.ascii_letters:
            result += i
    return result

print(not_in_alphabeth("AAsssss---AAhh:.n"))
