class Puppeteer:
    def __init__(self, name, len_beard, sneeze_count):
        self.name = name
        self.len_beard = len_beard
        self.sneeze_count = sneeze_count

    def wrap_his_beard(self, circumference):
        return self.len_beard // circumference

    def sneeze(self):
        return 'Sneeze' * self.sneeze_count

    def frustrate(self, arg):
        if arg % 2 == 0:
            self.sneeze_count += 1
        else:
            if self.sneeze_count > 0:
                self.sneeze_count -= 1

    def __str__(self):
        return 'Puppeteer ' + self.name + ', ' + str(self.len_beard) + \
               ', ' + str(self.sneeze_count)

    def __eq__(self, other):
        return self.name == other.name and self.len_beard == other.len_beard \
               and self.sneeze_count == other.sneeze_count

    def __lt__(self, other):
        if self.__eq__(other):
            return False
        else:
            if self.len_beard < other.len_beard:
                return True
            elif self.len_beard > other.len_beard:
                return False
            else:
                if self.sneeze_count < other.sneeze_count:
                    return True
                elif self.sneeze_count > other.sneeze_count:
                    return False
                else:
                    if len(self.name) < len(other.name):
                        return True
                    elif len(self.name) > len(other.name):
                        return False
                    else:
                        if self.name < other.name:
                            return True
                        elif self.name > other.name:
                            return False

    def __gt__(self, other):
        if self.__eq__(other):
            return False
        else:
            if self.len_beard > other.len_beard:
                return True
            elif self.len_beard < other.len_beard:
                return False
            else:
                if self.sneeze_count > other.sneeze_count:
                    return True
                elif self.sneeze_count < other.sneeze_count:
                    return False
                else:
                    if len(self.name) > len(other.name):
                        return True
                    elif len(self.name) < len(other.name):
                        return False
                    else:
                        if self.name > other.name:
                            return True
                        elif self.name < other.name:
                            return False

    def __le__(self, other):
        if self.__eq__(other):
            return True
        else:
            return self.__lt__(other)

    def __ge__(self, other):
        if self.__eq__(other):
            return True
        else:
            return self.__gt__(other)
