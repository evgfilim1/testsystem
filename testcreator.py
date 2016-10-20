fs = "task{}-test{}.{}"

for t in range(1, 5):
	for i in range(6):
		fints = open(fs.format(t, i, "in"), 'w')
		fouts = open(fs.format(t, i, "out"), 'w')

		ip = input("Enter app input (task {}, test {}): ".format(t, i))
		op = input("Enter app output (task {}, test {}): ".format(t, i))

		fints.write(ip)
		fouts.write(op)

		fints.close()
		fouts.close()
		
		print("------------")