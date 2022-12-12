# -*- coding: utf-8 -*-
# @Author: benjamin
# @Date:   2022-11-10 10:31:14
# @Device: MacOS
# @Last Modified by:   benjamin
# @Last Modified time: 2022-12-11 13:44:19
import numpy as np
import h5py as hp
from mpi4py import MPI

def test(data):
	GA = sum([abs(np.log10(j)) for j in data])
	RD = GA * np.random.random((7, 71, 1))
	return RD

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.rank
# name = MPI.Get_processor_name()

f = hp.File('Data.hdf5', 'a', driver='mpio', comm=comm)

coords_dset = f['test']
numRuns     = coords_dset.shape[0]
print(numRuns)
n           = numRuns // size
ans_dset    = f.create_dataset('answer', (7, 71, numRuns), dtype='float64')
print(ans_dset.shape)

idx = rank*n

coords  = coords_dset[idx:idx+n]

result = np.reshape(np.array([test(i) for i in coords]), (7, 71, n))

ans_dset[:, :, idx:idx+n] = result

f.close()