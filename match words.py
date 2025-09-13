def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) >= 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)

    print("list of words with first and last letter same\n:", lst)
    return
count = match_words(['abc', 'xyz', 'aba', '1221'])
print("Number of words with first and last letter same :", count)