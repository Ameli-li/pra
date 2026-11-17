from collections import Counter

text = input("Введите текст: ")
words = text.split()

unique = set(words)
counter = Counter(words)
repeated = {w: c for w, c in counter.items() if c > 1}

print("Всего слов:", len(words))
print("Уникальных слов:", len(unique))
print("Уникальные слова (по алфавиту):", sorted(unique))
print("Встречаются больше одного раза:", repeated)