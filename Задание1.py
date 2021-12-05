import pylab
import numpy as np
import json
import pathlib

A = 1.25313

def f(x): return 0.5 + (np.cos(np.sin(x ** 2 - A ** 2))**2 - 0.5) / (1 + 0.001 * (x ** 2 + A ** 2))

x_min = -100
x_max = 100
dx = 0.01
x = np.arange(x_min, x_max+0.01, dx)
y = f(x)

res = {
"data": [
{"x": float(x1), "y": float(y1)} for x1, y1 in zip(x, y)
]
}

path = pathlib.Path("results")
path.mkdir(exist_ok=True)
file = path / "result_task1.json"
out = file.open("w")
json.dump(res, out, indent=4)
out.close()

pylab.plot(x, y)
pylab.grid()
pylab.savefig("results/task1.png")
pylab.show()
