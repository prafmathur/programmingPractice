# Challenge #247 [Easy] Secret Santa
# https://www.reddit.com/r/dailyprogrammer/comments/3yiy2d/20151228_challenge_247_easy_secret_santa/

challengeInput = """Sean
Winnie
Brian Amy
Samir
Joe Bethany
Bruno Anna Matthew Lucas
Gabriel Martha Philip
Andre
Danielle
Leo Cinthia
Paula
Mary Jane
Anderson
Priscilla
Regis Julianna Arthur
Mark Marina
Alex Andrea"""

import random

names = challengeInput.split()
families = [set(l.split()) for l in challengeInput.splitlines()]

familyMembers = {}
familyNumber = 0
for name in names:
	if name not in families[familyNumber]:
		familyNumber+=1
	familyMembers[name] = families[familyNumber]

leftToPick = set(names)
secretSantas = {}
for name in names:
	secretSantas[name] = random.sample(leftToPick, 1)[0]
	while (secretSantas[name] in familyMembers[name]):
		secretSantas[name] = random.sample(leftToPick, 1)[0]
	leftToPick.remove(secretSantas[name])

for a,b in secretSantas.iteritems():
	print a + " -> " + b

# print families
