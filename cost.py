import time
import random

total = 0
before = time.perf_counter()
for i in range(1000000):
    total += random.randint(1, 100)
gaptime = time.perf_counter() - before
print("gaptime:", gaptime, flush=True)
