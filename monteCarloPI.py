import random

random.seed(318);

radius = 1
circNum = 0
trials = 1000000

for i in range(1,trials):
	x = random.random()
	y = random.random()
	rSqrt = x*x + y*y
	if rSqrt <= radius :
		circNum += 1

print((circNum / trials)*4)