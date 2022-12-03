# Без collections,
# подсчитывает количества вхождений каждой буквы, введенном тексте

text = input('Enter text: ')

data = [i: i for i in text]
data_key = data.keys()
data_char = data.values()

print(text)
print(data)
print(data_key)
print(data_char)
