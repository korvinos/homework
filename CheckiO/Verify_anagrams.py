def verify_anagrams(first_word, second_word):
    return sorted(''.join(first_word.lower().split())) == sorted(''.join(second_word.lower().split()))


print(verify_anagrams("Programming", "Gram Ring Mop"))
print(verify_anagrams("Hello", "Ole Oh"))
print(verify_anagrams("Kyoto", "Tokyo"))