text = input("Введите текст: ")
words = text.split()

print("Текст:", text)
print("1) Количество слов:", len(words))
if words:
    print("2) Первое слово:", words[0])
    print("3) Последнее слово:", words[-1])
    print("4) Обратный порядок:", words[::-1])
else:
    print("Текст пустой — слов нет.")


