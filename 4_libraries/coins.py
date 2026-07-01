import random

heads_count = 0
tails_count = 0

for _ in range(10000):
    coin = random.choice(['heads', 'tails'])
    if coin == 'heads':
        heads_count += 1
    else:
        tails_count += 1

print(f'head: {heads_count}\ntail: {tails_count}')

# as number of loop grow output from random tend to be
# uniform distribution for random.choice :D