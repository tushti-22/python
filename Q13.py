import os, time, random, string
import matplotlib.pyplot as plt

def random_text_mb(mb):
    N = mb * 1024 * 1024
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=N))

sizes = [1,2,4]
times = []

for s in sizes:
    fname = f"temp_{s}MB.txt"
    with open(fname,'w') as f:
        f.write(random_text_mb(s))
    t0 = time.time()
    with open(fname,'r') as f:
        data = f.read().upper()
    elapsed = time.time() - t0
    times.append(elapsed)
    os.remove(fname)
    print(f"Size {s}MB -> Time {elapsed:.3f}s")

plt.plot(sizes, times, marker='o')
plt.show()
