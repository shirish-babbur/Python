from sys import argv

def wc():
    line_count = 0
    word_count = 0
    char_count = 0

    command, filename = argv
    fileobj = open(filename, "r")

    data = fileobj.readlines()
    line_count = len(data)

    for line in data:
        if line is not "\n":
            words = line.split(" ")
            word_count += len(words)
            char_count += (len(line) - (len(words) - 1))

    print(f"""{filename} contains\n\nlines : {line_count}\nwords : {word_count}\nchars : {char_count}
            """)

wc()
