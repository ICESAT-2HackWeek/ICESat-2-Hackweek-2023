# Data Discovery and Access: Overview

## Learning Outcomes

The purpose of this overview is to introduce some of the data search and access options for ICESat-2 and other NASA data.

## Prerequisites

None

## Modes of Data Access

In the past, most of our scientific data analysis workflows have started with searching for data and then downloading that data to a local machine; whether that is the hard drive of your laptop or workstation, or some shared storage device hosted by your institution or research group.  This can be a time consuming process if the volume of data is large, even with fast internet.  It also requires that you have sufficient disk-space.  If you want to work with data from different geoscience domains, you may have to download data from several data centers.  I'll call this data access mode, the **download model** of data access.  

However, a change is a-foot.  New modes of data access are starting to becoming available.  Driven by the growth in the volume of data from future satellite missions, the archiving and distribution of NASA data is in a [state of transition](https://www.earthdata.nasa.gov/eosdis/cloud-evolution).  Over the next few years, all NASA data will be migrated to the NASA Earthdata Cloud, a cloud-hosted data store that will have all NASA datasets in one place.  This not only offers new modes of accessing NASA data but also offers new ways of working with this data.  As with Google Docs or Sheets, data in these "files" is not just stored in the cloud but compute resources offered by cloud providers allow you to process and analyze the data in the cloud.  When you edit your Google Doc or Sheet, you are working in the cloud not on your computer.  All you need is a web browser; you can work with these files on your laptop, tablet or even your phone. If you choose to share these documents with others, they can actively collaborate with you on the same document also in the cloud.  For large geoscience datasets, this means you can _skip the download_ and take your _analysis to the data_.  I'll call this data access mode **analysis in place**.

A third mode of access can be considered a hybrid of the **download model** and **analysis in place**.  I'll call this **data as a service**.  Often, we only need a subset of the data in a file.  Data for a select spatial region or time period, or only one or two variables.  Web-services like SlideRule have subsetting built-in to most of their APIs; and protocols such as OpenDAP have allowed subsetting for a long time.  By using cloud compute resources, we allow software to be run as a service to access and process cloud-hosted data, and then serve the processed data to a user as a subsetted and aggregated file.

During this transition period, data will be available from both the NASA DAACs (Distributed Active Archive Centers) that have archived and distributed data for over 20 years; and from cloud-hosted storage known as the Earthdata Cloud as data sets are migrated.  ICESat-2 data sets were some of the first data to be migrated to the cloud.  All Level-2 (e.g. ATL03 and beyond) ICESat-2 datasets are available in Earthdata Cloud. 

"The Cloud" is a somewhat nebulous term (pun intended).  In general, the cloud is a network of remote servers that run software and services that are accessed over the internet.  There is a growing number of commercial cloud providers (Google Cloud Services, Amazon Web Services, Microsoft Azure).  NASA has contracted with Amazon Web Services (AWS) to host data using the AWS Simple Storage Service (S3).  AWS offers a large number of services in addition to S3 storage.  A key service is Amazon Elastic Compute Cloud (Amazon EC2).  This is the service that is _under-the-hood_ of the CryoCloud JupyterHub you are using this Hackweek.  When you start a JupyterHub, an EC2 _instance_ is started.  You can think of an EC2 _instance_ as a remote computer.

AWS has the concept of a region, which is a cluster of data centers.  These data centers house the servers that run S3 and EC2 instances.  NASA Earthdata Cloud is hosted in the us-west-2 region.  This is important because if your EC2 instance is in the same region as the Earthdata Cloud S3 storage, you can access data in S3 directly in a way that is analogous to accessing a file on your laptop's or workstation's hard drive.  This is one of the key advantages of working in the cloud; you can do analysis where the data is stored without having to download the data to a local machine.  


```{table} Data Access Method and Tools
:name: data-access-overview-table

| | `icepyx` | `earthaccess` | Sliderule | OpenAltimetry | NASA Earthdata Search | NSIDC data product pages |
|:--- |:---:|:---:|:---:|:---:|:---:|:---:|
| Filter Spatially using:                     |   |   |   |   |   |   |
|    Interactive map widget                   |   |   | x | x | x | x |
|    Bounding Box                             | x | x | x | x | x | x |
|    Polygon                                  | x | x | x |   | x | x |
|    GeoJSON or Shapefile                     | x |   | x |   | x | x |
| Filter by time and date                     | x | x | x | x | x | x |
| Preview data                                | x | x |   | x | x | x |
| Download data from DAAC                     | x | x |   | x | x | x |
| Access cloud-hosted data                    | x | x | x |   | x |   |
| All ICESat-2 data                           | x | x |   |   | x | x |
| Subset (spatially, temporally, by variable) | x |   | x | x | _x_ |   |
| Load data by direct-access                  | x | x | x |   |   |   |
| Process and analyze data                    |   |   | x |   |   |   |
| Plot data with built-in methods             | x |   | x | x |   |   |
```
