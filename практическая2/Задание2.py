text = input("Введите текст: ")
words = text.split()

freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

for word, count in freq.items():
    print(f"{word} — {count}")

if freq:
    best = max(freq, key=freq.get)
    print("Самое частое слово:", best)