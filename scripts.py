import os

def insert_line_in_file(filename: str):
    with open(filename, "r", encoding="utf8") as f:
        contents = f.readlines()
    if len(contents) > 3:
        if "<html>" in contents[3]:
            contents.insert(4, "  <script>document.domain='sintef.energy';</script>\n")

    with open(filename, "w", encoding="utf8") as f:
        contents = "".join(contents)
        f.write(contents)

def insert_line_in_all_html(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".html"):
                print(os.path.join(root, file))
                insert_line_in_file(os.path.join(root, file))
