# Без collections,
# подсчитать количество вхождений каждой буквы, в введенном тексте

text = input('Enter text: ')

data = {i: text.count(i) for i in text}

print(data)
