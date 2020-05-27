def rjust_file(filename, len_just):
	f = open(filename, 'r')
	f_out = open('just_' + filename, 'w')
	for line in f:
		if line[0].isdigit():
			pos = line.find('.')
			num = line[:pos]
			num = num.rjust(len_just, '0')
			line = num + line[pos:]
		f_out.write(line)
	f_out.close()
	f.close()


rjust_file('enoh_new.txt', 3)
