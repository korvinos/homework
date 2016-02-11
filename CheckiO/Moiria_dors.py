def moria_key(text):
    data = text.lower().replace('.', '').split(' ')
    tab = {}
    for word in data:
        keys = text.lower().replace('.', '').split(' ')
        keys.remove(word)
        current = {}
        cor = 0
        print(keys)
        for key in keys:

            if word[1] == key[1]:
                cor += 10
            if word[-1] == key[-1]:
                cor += 10
            if len(word) <= len(key):
                cor += (len(word)/len(key))*30
            else:
                cor += (len(key)/len(word))*30
        tab[word] = current

    return tab


data = "Friend Fred and friend Ted."
print(list(moria_key(data)))
