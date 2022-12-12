import numpy as np
import h5py as hp

numRuns = 8
epsilon = 1.0e-2

A0   = np.random.uniform(1.0e-22, 0, numRuns)
A1   = A0 * (1  + epsilon * np.random.uniform(-1, 1, numRuns))
A2   = np.random.uniform(1.0e-22, 0, numRuns)
A3   = A2 * (1  + epsilon * np.random.uniform(-1, 1, numRuns))
A4   = np.random.uniform(1.0e-15, 0, numRuns)
A5   = A4 * (1  + epsilon * np.random.uniform(-1, 1, numRuns))
A6   = np.random.uniform(1.0e-14, 0, numRuns)
A7   = A6 * (1  + epsilon * np.random.uniform(-1, 1, numRuns))
A8   = np.random.uniform(1.0e-14, 0, numRuns)
A9   = A8 * (1  + epsilon * np.random.uniform(-1, 1, numRuns))
A10  = np.random.uniform(1.0e-14, 0, numRuns)
A11  = A10 * (1  + epsilon * np.random.uniform(-1, 1, numRuns))
A12  = np.random.uniform(1.0e-14, 0, numRuns)
A13  = A12 * (1  + epsilon * np.random.uniform(-1, 1, numRuns))
A14  = np.random.uniform(1.0e-14, 0, numRuns)
A15  = A14 * (1  + epsilon * np.random.uniform(-1, 1, numRuns))
file = hp.File('Data1.hdf5', 'w')
test = file.create_dataset("test", (numRuns, 16), dtype='float64')
test[...] = np.vstack((A0, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15)).T
file.close()
