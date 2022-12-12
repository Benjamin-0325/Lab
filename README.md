# h5py with mpi4py
---
* Data generator.py is a HDF5 data file generator, and MC new.py is a simple code for parallel HDF5.
* For each session, Data generator.py must be executed before MC new.py.
```shell
python3 Data\ generator.py
mpiexec -n 4 python3 MC\ new.py
```
