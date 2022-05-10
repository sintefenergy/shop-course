import os

def insert_line_in_file(filename: str, line_no: int, line_str: str):
    with open(filename, "r", encoding="utf8") as f:
        contents = f.readlines()

    contents.insert(line_no, line_str)

    with open(filename, "w", encoding="utf8") as f:
        contents = "".join(contents)
        f.write(contents)

def insert_line_in_all_html(folder):
    for file in os.listdir(folder):
        if file.endswith(".html") and not file.startswith("index"):
            print(os.path.join(folder, file))
            insert_line_in_file(
                os.path.join(folder, file),
                4,
                "  <script>document.domain='sintef.energy';</script>\n"
            )
