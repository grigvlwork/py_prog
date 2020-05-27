phrases = list()


def parrot(phrase):
    global phrases
    if phrase in phrases:
        print(phrase)
    else:
        phrases.append(phrase)
