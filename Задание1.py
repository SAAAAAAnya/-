import pylab
import numpy as np
import json
import pathlib

A = 1.25313

def f(x): return 0.5 + (np.cos(np.sin(x ** 2 - A ** 2))**2 - 0.5) / (1 + 0.001 * (x ** 2 + A ** 2))

x_min = -100
x_max = 100
dx = 0.01
x = np.arange(x_min, x_max, dx)
y = f(x)

res = {
"data": [
{"x": float(x1), "y": float(y1)} for x1, y1 in zip(x, y)
]
}

path = pathlib.Path("results")
path.mkdir(exist_ok=True)
file = path / "result_task1.json"
# 2 способ out = open(file, "w")
out = file.open("w")
# 2 способ file = open("result.json", "w")
# 2 способ file.write(json.dumps(res, indent=4))
json.dump(res, out, indent=4)
out.close()

pylab.plot(x, y)
pylab.grid()
# pylab.show()
pylab.savefig("results/task1.png")
