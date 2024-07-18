# H5Cloud - Cloud-Optimized Access of Hierarchical ICESat-2 Photon Data

## Team Members
* Project lead: Luis Lopez
* Project lead: Rachel Wegener
* JP Swinski
* Aimee Barciauskas
* Alex Lewandowski
* Jonathan Markel
* Suman Shekhar
* Andy Barrett

## Background
ICESat-2 photon-data is stored as HDF5 files, which provide many advantages for scientific applications including being self-describing and able to store heterogeneous data.
However, ICESat-2 granules are frequently over a larger spatial extent than is needed for scientific workflows, meaning users must read in the full ATL03 HDF5 file to geolocate the data, then subset to a given area of interest. Applications like EarthData and NSIDC data portals have simplified this process allowing users to subset files using a bounding box. 

Subsetting tools are not available when working in the cloud and directly access data stored in S3 buckets.  The reason for this is that HDF5 files are serialized.  HDF5 files stored in S3 buckets must be read fully into memory before they can be subsetted.  These file access patterns are often slower than working with files downloaded to local file systems. 

This is in contrast to raster data, where cloud-optimized GeoTIFFs are organized internally such that it is easy to access only a specific subset of the total area using HTTP GET range requests. A similar capability for ICESat-2 along-track photon data would provide measurable read performance improvements for cloud data providers and local data users alike. 

## Project Goals
The current aims of this Hackweek group are to benchmark current methods of accessing/ spatially subsetting ATL03 data from a public cloud data source (AWS S3), investigate methods of repacking photon data, and determine how libraries like [kerchunk](https://fsspec.github.io/kerchunk/) can be used for more efficient requesting of data from specific along-track locations.

## Project Outcomes [Pending]

List and describe, if desired, any project outcomes accomplished during the week.
These may be individual or aggregate, large or small.
The idea is to capture what your team learned and accomplished.
Links to relevant outputs are a great way to capture these outcomes, so long as the links are likely to remain valid for some time (this readme - with this list - will be archived as part of the Hackweek JupyterBook).
Some examples might be:

* We submitted a [Pull Request (PR) to the earthaccess library](https://nsidc.github.io/earthaccess/) to fix a typo.
* Kate opened a [discussion on icepyx](https://github.com/icesat2py/icepyx/discussions).
* Sam and Harvey put in a [SlideRule feature request](https://github.com/orgs/ICESat2-SlideRule/discussions).
* six team members wrote [functions for Pho](link to project team repository).
* We wrote a code block that finds the highest and lowest photon in a granule.
* [Example Workflow Jupyter Notebook](your notebook url here).
* We drafted a conference abstract for submission to [conference](https://www.agu.org/).


## Future Efforts

