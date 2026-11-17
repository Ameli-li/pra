with open("text.txt", encoding="utf-8") as f:
    content = f.read()

words = [w.strip(".,!?;:\"«»()—").lower() for w in content.split()]
words = [w for w in words if w]

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

print(f"{'Слово':<12}| {'Частота':>7}")
print("-" * 12 + "|" + "-" * 8)
for word, count in freq.items():
    print(f"{word:<12}| {count:>7}")