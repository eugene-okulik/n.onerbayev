# Task1
text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
    "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero"
)

text = text.split()

fintext = []

# Сделал сам.
for word in text:
    if word.endswith(','):
        fintext.append(word.replace(',', '') + 'ing')
    elif word.endswith('.'):
        fintext.append(word.replace('.', '') + 'ing')
    else:
        fintext.append(word + 'ing')
print(' '.join(fintext))


# Потом подумал как можно сделать лучше и гпт дал подсказку.
for word in text:
    annoying_word = word.rstrip(",.")
    fintext.append(annoying_word + "ing")
print(' '.join(fintext))
