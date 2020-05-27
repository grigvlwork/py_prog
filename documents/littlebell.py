class LeftParagraph:
    def __init__(self, width):
        self.width = width
        self.content = list()

    def add_word(self, word):
        if len(self.content) == 0:
            self.content.append(word)
        else:
            if len(self.content[-1]) + len(word) + 1 <= self.width:
                self.content[-1] = self.content[-1] + " " + word
            else:
                self.content.append(word)

    def end(self):
        for s in self.content:
            print(s)
        self.content = list()


class RightParagraph:
    def __init__(self, width):
        self.width = width
        self.content = list()

    def add_word(self, word):
        if len(self.content) == 0:
            self.content.append(word)
        else:
            if len(self.content[-1]) + len(word) + 1 <= self.width:
                self.content[-1] = self.content[-1] + " " + word
            else:
                self.content.append(word)

    def end(self):
        for s in self.content:
            print(' ' * (self.width - len(s)) + s)
        self.content = list()


rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()

