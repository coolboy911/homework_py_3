# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12

rus_alphabet = [
    "а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]
eng_alphabet = [
   "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
d = dict()
for el in ["A", "E", "I", "O", "U", "L", "N", "S", "T", "R", "А", "В", "Е", "И", "Н", "О", "Р", "С", "Т"]:
    d[el] = 1
for el in ["D", "G", "Д", "К", "Л", "М", "П", "У"]:
    d[el] = 2
for el in ["B", "C", "M", "P", "Б", "Г", "Ё", "Ь", "Я"]:
    d[el] = 3
for el in ["F", "H", "V", "W", "Y", "Й", "Ы"]:
    d[el] = 4
for el in ["K", "Ж", "З", "Х", "Ц", "Ч"]:
    d[el] = 5
for el in ["J", "X", "Ш", "Э", "Ю"]:
    d[el] = 8
for el in ["Q", "Z", "Ф", "Щ", "Ъ"]:
    d[el] = 10

# Проверка ввода
flag = True
while flag:
    word = input("введите слово: ").lower()
    if word[0] in rus_alphabet:
        for letter in word[1:]:
            if letter not in rus_alphabet:
                print("Неправильно введено слово")
                break
        else: 
            flag = False
    elif word[0] in eng_alphabet:
        for letter in word[1:]:
            if letter not in eng_alphabet:
                print("Неправильно введено слово")
                break
        else: 
            flag = False
    else:
        print("Неправильно введено слово")

# подсчет
word = word.upper()
total = 0
for letter in word:
    total += d[letter]
print(total)