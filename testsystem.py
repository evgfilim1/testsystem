import os, subprocess, logging

fs = "task{}-test{}.{}"

errors = [0, 0, 0, 0]
success = [0, 0, 0, 0]

logging.basicConfig(level=logging.INFO, format="%(levelname)-1s: %(message)s")

for t in range(1, 5):
	for i in range(6):
		print()
		logging.info("Task {}, test {}".format(t, i))
		fints = open(fs.format(t, i, "in"), 'r')
		with open(fs.format(t, i, "out"), 'r') as fo:
			outs = fo.read()

		proc = subprocess.Popen("Task{}-compiled.exe".format(t), stdin=fints, stdout=subprocess.PIPE,
			universal_newlines=True, stderr=subprocess.PIPE)
		try: 
			appfds = proc.communicate(timeout=5)
		except TimeoutExpired:
			logging.error("Terminated by timeout")
			proc.kill()
			appfds = proc.communicate()

		if proc.returncode != 0:
			logging.warning("Terminated with signal {}".format(proc.returncode))

		if appfds[0] != outs:
			logging.error("Answer is wrong!")
			logging.info("Right: {}\nProgram: {}".format(outs, appfds[0]))
			errors[t - 1] += 1
		else:
			logging.info("Answer is right!")
			logging.debug("Answer:{}".format(outs))
			success[t - 1] += 1

		if appfds[1] != '':
			logging.info("Errors generated: {}\n".format(appfds[1]))

print('\n=====STATS=====')
logging.info("Success: {}, With errors: {}".format(success, errors))
print()
p = 0; t = 0
for i in success:
	p += i
for i in errors:
	t += i
t += p
logging.info('Solved: {}%'.format(p / t * 100))