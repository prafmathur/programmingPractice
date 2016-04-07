import hashlib


m = hashlib.md5()

counter = 0
while True:
	if hashlib.md5("ckczppom" + str(counter)).hexdigest()[0:6] == "000000":
		print counter
		break
	counter += 1