with open('poem.txt', 'r', encoding='utf-8') as file:
    text = file.read()

print(text, end='\n\n')

vowel_words = 0
consonants_words = 0
specitial_sumvol = 0

text_for_interation = list(text.lower().split())

for el in text_for_interation:
    if el.startswith('a'):
        vowel_words += 1
    elif el.startswith('я'):
        vowel_words += 1
    elif el.startswith('о'):
        vowel_words += 1
    elif el.startswith('ё'):
        vowel_words += 1
    elif el.startswith('е'):
        vowel_words += 1
    elif el.startswith('э'):
        vowel_words += 1
    elif el.startswith('у'):
        vowel_words += 1
    elif el.startswith('ю'):
        vowel_words += 1
    elif el.startswith('ы'):
        vowel_words += 1
    elif el.startswith('и'):
        vowel_words += 1
    elif el.startswith('\"и'):
        vowel_words += 1
    elif el.startswith('-'):
        specitial_sumvol += 1
    else:
        consonants_words += 1

print(specitial_sumvol)
if vowel_words > consonants_words:
    print(f'Слов на гласных больше: {vowel_words} против {consonants_words}.')
elif vowel_words < consonants_words:
    print(f'Слов на согласных больше: {consonants_words} против {vowel_words}.')
elif vowel_words == consonants_words:
    print(f'Слов на гласных и согласных поравну: {vowel_words} = {consonants_words}.')

