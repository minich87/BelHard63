split_file = int(input('Enter a number to split: '))

with open('file_with_few_strings.txt', 'r', encoding='utf-8') as file:
    text = [line.strip() for line in file if line.strip()]

text_add = [' '.join(text[split_file - 1:])]
new_text = text[:split_file - 1] + text_add

i = 0
while i < split_file:
    name_file = f'new_file_{1 + i}.txt'
    with open(name_file, 'w', encoding='utf-8') as file:
        file.write(new_text[i])
        i += 1
