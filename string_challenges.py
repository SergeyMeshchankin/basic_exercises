# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
count = word.lower().count('а')
print(count)

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
vowels = 'аеёиоуыэюя'
count = sum(1 for letter in word.lower() if letter in vowels)
print(count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
words = sentence.split()
print(len(words))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
for word in sentence.split():
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
words = sentence.split()
average_length = sum(len(word) for word in words) / len(words)
print(average_length)
