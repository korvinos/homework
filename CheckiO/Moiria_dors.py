def moria_key(text):
    text = text.lower().replace('.', '').split(' ')
    tab = {}
    for word in text:

        current = {}
        cor = 0

        for key in text:

            if word[1] == key[1]:
                cor += 10
            if word[-1] == key[-1]:
                cor += 10
            if len(word) <= len(key):
                cor += (len(word)/len(key))*30
            else:
                cor += (len(key)/len(word))*30

            current[key] = cor
        tab[word] = current

    return tab


data = "Friend Fred and friend Ted."
print(list(moria_key(data)))
