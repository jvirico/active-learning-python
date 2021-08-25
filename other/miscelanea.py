### adding a progress bar to for loops
# source: https://www.youtube.com/watch?v=FptVpIPhdpM&t=107s

from tqdm import tqdm, trange
import time

for i in tqdm(range(100)):
    time.sleep(0.01)

for i in trange(100):
    time.sleep(0.01)

with tqdm(total=100) as pbar:
    for i in range(10):
        time.sleep(0.3)
        pbar.update(10)

pbar = tqdm(total=100)
for i in range(10):
    time.sleep(0.3)
    pbar.update(10)
pbar.close()