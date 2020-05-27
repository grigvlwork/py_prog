friends = dict()


def add_friends(name_of_person, list_of_friends):
    global friends
    if name_of_person not in friends.keys():
        friends[name_of_person] = list_of_friends
    else:
        friends[name_of_person] += list_of_friends


def are_friends(name_of_person1, name_of_person2):
    global friends
    if name_of_person1 not in friends.keys():
        return False
    else:
        if name_of_person2 not in friends[name_of_person1]:
            return False
        else:
            return True


def print_friends(name_of_person):
    global friends
    if name_of_person not in friends.keys():
        print()
    else:
        print(' '.join(sorted(friends[name_of_person])))
