# Python program that repeatedly reads lines from standard
def read_eof():
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        for line in reversed(lines):
            print(line)


read_eof()
