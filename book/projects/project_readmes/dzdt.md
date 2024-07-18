# dzdt

## Team Members

The following people contributed to our project throughout the week:
* Project lead: [Joanmarie Del Vecchio](https://jmdelvecchio.github.io/)
* Helper: [Scott Henderson](https://github.com/scottyhq)
* Helper: [Shashank Bhushan](https://github.com/ShashankBice)
* Team member: [Matt Olson](url to their webpage)

## Project Goals

In addition to learning more about working with ICESat-2 data on the cloud, our goals are to explore
permafrost and land surface change with crossover ATL06 data

## Project Outcomes

* Created a GitHub Repository with Jupyter Notebooks detailing exploratory analysis at several areas of interest in the Arctic https://github.com/ICESAT-2HackWeek/dzdt

* Closed a SlideRule GitHub Issue related to raster sampling of new ArcticDEM v4.1 release (https://github.com/ICESat2-SlideRule/sliderule/issues/299#issuecomment-1674246119)

* Contributed to notes on 3D Geodetic transforms to inter-compare various elevation datasets https://github.com/ICESAT-2HackWeek/3D_CRS_Transformation_Resources
* The group has learned more about working with cloud-hosted data and visualization techniques with geodataframes
* Joanmarie wrote a script that ingests a GeoJSON area of interest (AOI) which then (1) queries the [MODIS daily snow cover product](https://nsidc.org/data/mod10a1/versions/6) via Earth Engine and filters for"low-snow" dates over the study area, (2) queries `sliderule` for ATL06 tracks for the same AOI and filters the track collection dates to only those "low-snow" dates, (3) finds overlapping footprints from remaining measurements and differences the heights, and (4) creates an interactive Earth Engine and geopandas map that displays imagery from the lowest-snow days along with calculated height differences as proof-of-concept and for studying feasibility. 

  to acquire ATL06 crossovers for dzdt 
* Reported bugs in [sliderule example documentation](https://github.com/ICESat2-SlideRule/sliderule/issues/300) and [icepyx tutorial](https://github.com/ICESAT-2HackWeek/ICESat-2-Hackweek-2023/pull/82).
## Future Efforts

We will continue to investigate elevation changes from ICESat-2 only (repeat tracks and crossovers), as well as comparing ICESat-2 with other time-dependent elevation data (ArcticDEM, InSAR)

The team plans to stay connected via GitHub and Slack and share periodic updates. We think there is high potential for an AGU abstract in 2024 and even a manuscript! 
