split_file = int(input('Enter number strings: '))

with open('file_with_few_strings.txt', 'r', encoding='utf-8') as file:
    text = [line.strip() for line in file if line.strip()]

text_add = [' '.join(text[split_file - 1:])]

new_text = text[:split_file - 1] + text_add

with open('new_file.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(new_text))
