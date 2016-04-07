niceStrings = 0

with open("nicestr.txt") as f:
	for s in f:
		if s.count("a") + s.count("e") + s.count("i") + s.count("o") + s.count("u") < 3:
			continue
		appearsTwice = False
		noBad = True
		for i in xrange(len(s)-1):
			if(s[i:i+1] in ["ab", "cd", "pq", "xy"]):
				noBad = False
			if(s[i] == s[i+1]):
				appearsTwice = True

		if appearsTwice and noBad:
			niceStrings += 1

print niceStrings