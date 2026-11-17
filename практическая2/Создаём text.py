text_txt = """Мама мыла раму.
Мама мыла раму очень чисто.

Рама была чистая."""

with open("text.txt", "w", encoding="utf-8") as f:
    f.write(text_txt)

corpus_part = """Мама мыла раму. Рама была чистая и блестящая.
Мыла раму мама, а потом мыла окно. Окно было чистое.
За окном всё шёл и шёл дождь, а мы сидели и смотрели на мокрую улицу.
"""

with open("corpus.txt", "w", encoding="utf-8") as f:
    f.write(corpus_part * 3)

print("Файлы text.txt и corpus.txt созданы")