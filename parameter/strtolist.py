def from_string_to_list(string, container):
    container.extend([int(s) for s in string.split()])
