import re
from collections import Counter

with open("corpus.txt", encoding="utf-8") as f:
    corpus = f.read()

tokens = re.findall(r"[а-яёa-z]+(?:-[а-яёa-z]+)*", corpus.lower())
cnt = Counter(tokens)

total = len(tokens)
uniq = len(cnt)
avg_len = sum(len(w) for w in tokens) / total if total else 0
top10 = cnt.most_common(10)

lines_out = [
    "ОТЧЁТ ПО КОРПУСУ corpus.txt",
    f"Всего слов: {total}",
    f"Уникальных слов: {uniq}",
    f"Средняя длина слова: {avg_len:.2f}",
    "Топ-10 частых слов:",
]
for i, (w, c) in enumerate(top10, 1):
    lines_out.append(f"{i:>2}. {w:<15} {c:>5}")

report = "\n".join(lines_out)
print(report)
with open("report.txt", "w", encoding="utf-8") as f:
    f.write(report + "\n")
print("\nОтчёт сохранён в report.txt")