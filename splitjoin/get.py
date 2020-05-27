url = input()
key = input()
keys = url.split("?")[1].split("&")
for item in keys:
    if item.split("=")[0] == key:
        print(item.split("=")[1])
        break
