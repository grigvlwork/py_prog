class Storm:
    def __init__(self, speed, content):
        self.speed = speed
        self.content = content

    def __str__(self):
        return 'Storm ' + str(self.speed) + ', ' + str(len(self.content))

    def str(self):
        return self.__str__()

    def values(self):
        return self.content

    def velocity(self):
        return self.speed

    def change_vel(self, value):
        self.speed += value
        if self.speed <= 0:
            self.content = list()

    def __getitem__(self, key):
        return self.content[key]

    def __setitem__(self, key, value):
        self.content[key] = value

    def append(self, value):
        self.content.append(value)

    def __delitem__(self, key):
        self.content.pop(key)

    def __len__(self):
        return len(self.content)

    def __contains__(self, item):
        return item in self.content

    def __add__(self, other):
        c = self.content + other.content
        s = (self.speed + other.speed) // 2
        return Storm(s, c)

    def __rshift__(self, n):
        new_content = [0] * len(self.content)
        for i in range(len(self.content)):
            new_content[(i + n) % len(self.content)] = self.content[i]
        self.content = new_content

    def __lshift__(self, n):
        d = len(self.content)
        new_content = [0] * d
        for i in range(d):
            new_content[(i - n + d) % d] = self.content[i]
        self.content = new_content

    def __call__(self, x):
        return min(self.content[:x])
