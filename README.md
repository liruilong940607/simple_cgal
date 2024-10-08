# simple_cgal
A wrapper to perform 2D/3D Delaunay triangulation using CGAL with pybind11 and CMake. Supports distributed memory parallel Delaunay triangulation using (for now qhull)

# Dependencies
Note `boost` and `gmp` are required to exist in the system, which can be installed via `sudo apt-get install libboost-all-dev libgmp3-dev` on Linux.


# Installation
1. clone the repo: ```git clone --recursive https://github.com/liruilong940607/simple_cgal.git```
2. run: ```pip install pybind11 cmake; pip install .```

# How does it work?

```python
 import random
 
 import numpy
 import simple_cgal
 
 import time
 
 num_points = 1000
 points = numpy.array([(random.random()*1.0, random.random()*1.0) for _ in range(num_points)])
 
 t1 = time.time()
 faces = simple_cgal.delaunay2(points[:,0],points[:,1])
 print('elapsed time is '+str(time.time()-t1))
 
 import matplotlib.pyplot as plt
 plt.triplot(points[:,0], points[:,1], faces)
 plt.show()
```

