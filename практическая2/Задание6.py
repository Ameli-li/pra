import time, random

def pairs_naive(words):
    pairs = 0
    n = len(words)
    for i in range(n):
        for j in range(i + 1, n):
            if words[i] == words[j]:
                pairs += 1
    return pairs

def pairs_dict(words):
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return sum(c * (c - 1) // 2 for c in freq.values())

text = input("Введите текст: ")
words = text.split()
print("Пары (наивно):", pairs_naive(words))
print("Пары (через словарь):", pairs_dict(words))

random.seed(42)
pool = [f"слово{i}" for i in range(200)]
print(f"{'n':>7} | {'наивно, с':>10} | {'словарь, с':>11}")
for n in (1000, 5000, 10000):
    data = [random.choice(pool) for _ in range(n)]
    t0 = time.perf_counter(); a = pairs_naive(data); t1 = time.perf_counter()
    b = pairs_dict(data); t2 = time.perf_counter()
    print(f"{n:>7} | {t1-t0:>10.4f} | {t2-t1:>11.6f} | совпало: {a == b}")