text = input("Введите текст: ")
words = text.split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

with open("freq.txt", "w", encoding="utf-8") as f:
    for word, count in freq.items():
        f.write(f"{word} — {count}\n")

print("Результат сохранён в freq.txt")
print(open("freq.txt", encoding="utf-8").read())     