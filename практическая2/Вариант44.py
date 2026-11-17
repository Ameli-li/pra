text = input("Введите текст: ")
words = text.split()
print("\nОбратный алфавитный порядок:")
print("Обратный порядок:", sorted(words, key=str.lower, reverse=True))

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

capitalized = [w for w in freq if w[0].isupper()]
print("\nСлова с заглавной буквы:", capitalized)
print("Их количество:", len(capitalized))

VOWELS = set("аеёиоуыэюя")
vowel_end = sorted({w.lower() for w in words if w[-1].lower() in VOWELS})
print("\n Слова на гласную в конце:", vowel_end)
print("Их количество (уникальных):", len(vowel_end))

vowel_count = sum(1 for c in text.lower() if c in VOWELS)
print("\n Количество гласных:", vowel_count)

with open("freq.txt", "w", encoding="utf-8") as f:
    for i, (word, count) in enumerate(freq.items(), 1):
        f.write(f"{i}. {word} — {count}\n")



print("\nРезультат с нумерацией сохранён в freq.txt")

import random, tracemalloc

random.seed(42)
pool = [f"слово{i}" for i in range(200)]
big_words = [random.choice(pool) for _ in range(10000)]

tracemalloc.start()
pairs_naive = 0
n = len(big_words)
for i in range(n):
    for j in range(i + 1, n):
        if big_words[i] == big_words[j]:
            pairs_naive += 1
current, peak_naive = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
freq_big = {}
for w in big_words:
    freq_big[w] = freq_big.get(w, 0) + 1
pairs_dict = sum(c * (c - 1) // 2 for c in freq_big.values())
current, peak_dict = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("\nЗамер памяти (tracemalloc), n = 10000:")
print("Пар найдено наивно:", pairs_naive, "| через словарь:", pairs_dict)
print(f"Наивный алгоритм: {peak_naive / 1024:.1f} КБ")
print(f"Словарь:          {peak_dict / 1024:.1f} КБ")

GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print("\nТаблица с цветом:")
print(f"{'Слово':<12}| {'Частота':>7}")
print("-" * 12 + "|" + "-" * 8)
for word, count in freq.items():
    color = GREEN if count > 1 else YELLOW
    print(color + f"{word:<12}| {count:>7}" + RESET)

import matplotlib.pyplot as plt

top10 = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:10]

plt.figure(figsize=(10, 5))
plt.bar([w for w, c in top10], [c for w, c in top10], color="green", edgecolor="black")
plt.title("Гистограмма частот слов")
plt.xlabel("Слово")
plt.ylabel("Частота")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("hist.png", dpi=150)
plt.show()

print("\nГистограмма сохранена в hist.png")