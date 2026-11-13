import csv #подключает встроенный модуль для создания и записи таблиц в формате CSV
import docx # подключает библиотеку для чтения вордовский доков
import matplotlib.pyplot as plt #подключает библиотеку для рисования графиков
doc = docx.Document("lion.docx") #открывает файл и сохраняет его содержимое в переменную 
list = [] #создает пустой список куда будут складываться все абзацы текста
for paragraph in doc.paragraphs: #запускает цикл, который по очереди берет каждый абзац из дока
    list.append(paragraph.text) #извлекает чистый текст из текущего абзаца и добавляет его в список 
full_l = " ".join(list).lower() #склеивает все абзацы из списка в одну сплошную строку через пробел и делает буквы маленькими
clean_t = "" #создает пустую строку для очищенного текста
for i in full_l: #запускает цикл для проверки каждого символа в тексте.
    if i.isalpha() or i.isspace(): #проверяет является ли символ буквой или пробелом
        clean_t += i #если символ прошел проверку дописывает его в конец чистой строки 
words = clean_t.split() #разделяет текст по пробелам и получает список всех отдельных слов
total_words = len(words) 
unique_words = [] #создает пустой список для хранения слов без повторов
for word in words: # перебирает каждое слово
    if word not in unique_words: #проверяет нет ли этого слова уже в списке
        unique_words.append(word) #если слово встретилось впервые добавляет его в список
word_stats = [] #создает пустой список для таблицы
for word in unique_words: #запускает цикл по каждому уникальному слову
    freq = words.count(word) #считает сколько раз слово встретилось в списке
    p = round((freq / total_words) * 100, 2) #вычисляет долю слова в процентах
    word_stats.append([word, freq, p])
csv_file = open("words_stat.csv", "w", encoding="utf-8-sig", newline="")
writer = csv.writer(csv_file, delimiter=";")
writer.writerow(["Слово", "Частота встречи, раз", "Частота встречи в %"])
writer.writerows(word_stats) #записывает все собранные данные
csv_file.close()
letters = [char for char in clean_t if char.isalpha()] #создает список всех букв
unique_letters = []
for letter in letters:
    if letter not in unique_letters: #проверяет не добавлена ли эта буква ранее
        unique_letters.append(letter)
letter_counts = []
for letter in unique_letters:
    letter_counts.append(letters.count(letter)) #считает сколько раз буква встречается в тексте
plt.figure(figsize=(12, 6))
plt.bar(unique_letters, letter_counts, color="skyblue", edgecolor="black")
plt.title("Частота встречаемости букв в тексте")
plt.xlabel("Буквы")
plt.ylabel("Количество раз")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
