prev_message = ''


def print_without_duplicates(message):
    global prev_message
    if message != prev_message:
        print(message)
        prev_message = message
