import sys

lines = [line for line in sys.stdin if len(line) > 0]
words = []
for line in lines:
	temp = c = line[0]
	for i in range(1, len(line)):
		if isalpha(line[i]):
			temp += line[i]
		else:
			if len(temp) > 0:
				words.append(temp)
				temp = ''
	if len(temp) > 0:
		words.append(temp)
		temp = ''
words = enumerate(words)
words.sort()

