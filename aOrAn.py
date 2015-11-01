def aOrAn(word):
    if len(word) > 0:
        if word[0] in 'aeiou':
            return 'an'
        else:
            return 'a'
    else:
        return 'a'
