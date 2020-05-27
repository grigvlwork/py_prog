height = int(input())
width = int(input())
smb = input()
if height == 1:
    print(smb * width)
else:
    print(smb * width)
    if width == 1:
        for i in range(height - 2):
            print(smb)
    else:
        for i in range(height - 2):
            print(smb + " " * (width - 2) + smb)
    print(smb * width)
