import random
import math
random.seed(11)
def fn(x):
	return 0.2+25.*x - 200.*x**2. + 675.*x**3. -900.*x**4. + 400.*x**5.

b = 0.8
a = 0.
N = 3000.
summ = 0.
for i in range(int(N)):
	temp = random.random()*(0.8)
	summ = summ+ fn(temp)
summ = summ/N
print ((b-a)*summ)
