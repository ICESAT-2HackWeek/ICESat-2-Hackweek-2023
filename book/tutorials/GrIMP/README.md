# GrIMPNotebooks 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fastice/GrIMPNotebooks/HEAD?urlpath=lab) (potentially faster)

[![Binder](https://gesis.mybinder.org/badge_logo.svg)](https://gesis.mybinder.org/v2/gh/fastice/GrIMPNotebooks/HEAD?urlpath=lab) (more memory)

Notebooks for working with Greenland Ice Mapping Project (GrIMP) data archived at NSIDC, which are funded by the NASA [MEaSUREs](https://earthdata.nasa.gov/esds/competitive-programs/measures) program.

## Binder

These notebooks can run locally on a users own machine or cloud resource, but users can also run them remotely free of charge as a [*binder*](https://jupyter.org/binder) app. Advantages to *binder* are:
- The notebook runs in a well-tested, pre-configured environment,
- No need to setup on your own machine.

There are some limitations to *binder*:
- The *binder* instances are often limited to 2GB of memory, which can easily be exceeded if too large a region is or too many products are selected.
- The *binder* instance will time out after an ten minutes of inactivity, and all work will be lost. Keeping the notebook in the foreground while it runs should avoid a timeout. 

To run the notebooks, click on the launchbinder button at the top of this file.

## Installation on Local Machine

If not running in binder, the easiest and surest way to run these notebooks is use create a [conda](https://docs.conda.io/en/latest/) environment using the [environment.yml](https://github.com/fastice/GrIMPNotebooks/blob/master/binder/environment.yml) file in the binder folder for this repository.

    conda env create -f environment.yml
    python -m ipykernel install --user --name=greenlandMapping

Once installation is complete:

    conda activate greenlandMapping
    jupyter lab
    
The code in these notebooks requires two code from three repositories: [GrIMPfunc](https://github.com/fastice/GrIMPfunc), [nisardev](https://github.com/fastice/nisardev), and [gimpqgis](https://github.com/fastice/gimpqgis). The latter is needed only for the [qgisRremoteNotebook.ipynb](https://github.com/fastice/GrIMPNotebooks/blob/master/qgisRemoteNotebook.ipynb) notebook. These packages are install automatically with conda install described above.

## [NSIDCLoginNotebook.ipynb](https://github.com/fastice/GrIMPNotebooks/blob/master/NSIDCLoginNotebook.ipynb) - Start Here!

This notebook contains a lot of information about setup and lets the user test the NSIDC login. If the environment is up and running (e.g., if launched from binder), then it can be skipped.

This notebook creates a cookie file and .netrc file with authentication information that GDAL based programs (e.g., other Notebooks in this repo and *QGIS*) can download /vsicurl links to allow remote access of data archive at NSDIC. The notebook contains full setup instructions. Users should view the notebook on github before trying to run.

The directions for setup are contained in the notebook, so its a good idea to read the github rendered notebook before proceeding.

This notebook can also setup the login authentication for *QGIS* for remotely viewing the products at NSIDC.

## [workingWithGrIMPVelocity.ipynb](//github.com/fastice/GrIMPNotebooks/blob/master/workingWithGrIMPVelocity.ipynb)

This notebook demonstrate much of the functionality of the nisarVel and nisarVelSeries ([nisardev](https://github.com/fastice/nisardev)) classes for working with GrIMP velocity data remotely to create publication ready plots.

## [workingWithGrIMPImageData.ipynb](//github.com/fastice/GrIMPNotebooks/blob/master/workingWithGrIMPImageData.ipynb)

This notebook demonstrate much of the functionality of nisarImageSeries ([nisardev](https://github.com/fastice/nisardev)) classes for working with GrIMP image data remotely to create publication ready plots.

## [Flowlines.ipynb](https://github.com/fastice/GrIMPNotebooks/blob/master/Flowlines.ipynb)

This notebook demonstrates how Greenland Ice Mapping Project can be remotely accessed to create plots along flowlines from Felikson et al., 2020, which are archived on Zenodo. The copies of the shapefiles included in this repository were downloaded in late January 2022.

It allows generation of flowline and time series plots for any of the glaciers in the Felikson shape files (essentially all major glaciers).

## [GrIMPSubsetterNotebook.ipynb](https://github.com/fastice/GrIMPNotebooks/blob/master/GrIMPSubsetterNotebook.ipynb)

This notebook allows users to download subsets of [GrIMP](https://nsidc.org/data/measures/gimp) image ([NSIDC-0723](https://nsidc.org/data/nsidc-0723)) and velocity ([NSIDC-481](https://nsidc.org/data/nsidc-0481), [0725](https://nsidc.org/data/nsidc-0725), [0727](https://nsidc.org/data/nsidc-0727), [0731](https://nsidc.org/data/nsidc-0731), and [0766](https://nsidc.org/data/nsidc-0766)) data. This process allows relatively small downloads for individual glaciers rather than having to download full Greenland datasets, which can exceed 2TB.

For the Sentinel based velocity mosaics (0725, 0727, 0731, and 0766), the user can select a box for their area of interest (AOI) on a map and then select which components are required (vv, vx, vy, ex, ey, dT). The selected data are the downloaded and saved to a netCDF file. Users can explore the data by interactively selecting points that are plotted as time series. In the case of the TSX products (NSDIC-0481), given their small size, the full product "box" is downloaded. Because of the sparse nature of these boxes, only the the products associated with a single box can be downloaded at a time.

## [qgisRremoteNotebook.ipynb](https://github.com/fastice/GrIMPNotebooks/blob/master/qgisRemoteNotebook.ipynb)

This notebook has a search tool to search for *GrIMP* products at NSIDC. Following the search, the result can automically be incorporated in a new *QGIS* project that accesses the data remotely. It can also group and save the data as *QGIS Layer Definition Files*, which allow subsets of the data to easily be imported into an existing *QGIS* project.

## Caveats

The remote access functions for these notebooks will require the user to have a freely available [NASA Earth Data Login](https://urs.earthdata.nasa.gov).

These notebooks rely on http network transfers, which can be flaky. So for some crashes, you need not be crazy to repeat the same procedure over and over and expect a different result (at least not for the first few tries).
