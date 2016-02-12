def checkio(first, second):
    words = first.split(',') + (second.split(','))
    return ','.join(sorted(list(filter(lambda x: words.count(x) != 1, set(words)))))

print(checkio("one,two,three", "four,five,one,two,six,three"))
