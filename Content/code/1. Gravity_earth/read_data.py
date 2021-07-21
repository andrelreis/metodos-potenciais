import numpy as np
import xarray as xr

def fetch_dataset(fname):
    data = xr.open_dataset(fname)
    # Capture attributes dict because it's removed after converting the data to
    # float64
    attrs = data.attrs.copy()
    # The data are stored as ints and data as float32 to save space on the
    # data file. Cast them to float64 to avoid integer division errors.
    data = data.astype("float64")
    data.attrs = attrs
    return data