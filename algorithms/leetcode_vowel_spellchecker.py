def vowel_spellchecker(word_list, queries):
    vowels = set("aeiou")
    words = set(word_list)

    lower_map = {}
    for word in word_list:
        lower_map.setdefault(word.lower(), word)

    def censor_vowels(text):
        return "".join("*" if c in vowels else c for c in text.lower())

    vowel_map = {}
    for word in word_list:
        vowel_map.setdefault(censor_vowels(word), word)

    result = []
    for query in queries:
        if query in words:
            result.append(query)
        elif query.lower() in lower_map:
            result.append(lower_map[query.lower()])
        elif censor_vowels(query) in vowel_map:
            result.append(vowel_map[censor_vowels(query)])
        else:
            result.append("")
    return result


print(vowel_spellchecker(["KiTe", "kite", "hare", "Hare"],
                         ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]))
print(vowel_spellchecker(["yellow"], ["YellOw"]))
print(vowel_spellchecker(["zeo", "Zuo"], ["zuo"]))
