c = input()
print("\n".join([s for s in input().split() if s.lower().find(c) > -1]))
