inp = open('3.in', 'a+')

size = 100000
bound = 1000000000
inp.write('\n')
inp.write(str(size) + '\n')
import random

order = [i + 1 for i in range(size)]
random.shuffle(order)
order = map(str, order)
for i in range(size):
  val = random.randint(0, bound)
  inp.write(str(val) + ' ')
inp.write('\n')
inp.write(' '.join(order) + '\n')
inp.close()
