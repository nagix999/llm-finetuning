
def read_file(file):
    with open(file, "r", encoding="utf-8") as f:
        contents = f.read()
        return contents