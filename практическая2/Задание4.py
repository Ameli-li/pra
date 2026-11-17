with open("text.txt", encoding="utf-8") as f:
    content = f.read()

lines = content.splitlines()
words = content.split()

print("Файл: text.txt")
print("Количество строк:", len(lines))
print("Количество слов:", len(words))
print("Количество символов (с пробелами и переносами):", len(content))
print("Количество символов без пробелов и переносов:", len("".join(content.split())))