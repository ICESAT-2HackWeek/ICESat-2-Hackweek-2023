# Data Access and Formats

There is a host of different ways to access ICESat-2 data in particular and NASA data in general.  This section provides a map to the current (as of August 2023) landscape of data access methods.  It also provides an introduction to HDF5 and NetCDF, the file formats that ICESat-2 data products are stored in.  The focus is on accessing data from a cloud compute instance in AWS us-west-2.  However, some of the access methods and tools can be used from a local machine as well.

The tutorials are organized as follows:

- [Overview](tutorials/data-access-and-format/overview) provides an introduction to data access tools and offers some guidance on the capabilities and applicability of the different tools.
- [EarthData Search](tutorials/data-access-and-format/earthdata-search) is a GUI search interface for NASA data.  This is probably the simplest way to search for ICESat-2 and other NASA data.
- [`earthaccess`](tutorials/data-access-and-format/earthaccess) is a Python package to search for NASA datasets and granules, and to download those granules, or, if you are in  AWS `us-west-2` cloud compute instance, open data files directly from cloud storage.
- [`icepyx`]() is a data search and access tools specifically for ICESat-2
- [Sliderule]() is a ...