# Написать функцию для кодировки текста в соответствии с кодом Морзе

morses_code = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': '|',
    }


def text_to_morse(text):
    global morses_code
    text = text.upper()
    morse = ''
    for i in text:
        morse += morses_code.get(i, ' ')
        morse += ' '
    return  morse

def morse_to_text(morse):
    global morses_code
    morse = morse.replace('|', '|')
    text = ''
    for el in morse.split():
        for key, val in morses_code.items():
            if el == val:
                text += key
                continue
    return text

print(text_to_morse('Hello World!'))
print(morse_to_text('.... . .-.. .-.. --- | .-- --- .-. .-.. -.. '))
