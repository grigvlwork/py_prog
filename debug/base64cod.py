import base64
s = input()
while len(s) > 0:
    print(base64.b64encode(bytes(s, 'utf-8')))
    s = input()


