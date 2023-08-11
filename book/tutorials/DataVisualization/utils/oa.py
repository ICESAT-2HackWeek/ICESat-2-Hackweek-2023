import os
import ee
import geemap
import json
import requests
import numpy as np
import pandas as pd
import matplotlib 
import matplotlib.pylab as plt
from datetime import datetime
from datetime import timedelta
import rasterio as rio
from rasterio import plot as rioplot
from rasterio import warp
import traceback

try:
    ee.Initialize()
except: 
    ee.Authenticate()
    ee.Initialize()

class dataCollector:
    def __init__(self, beam=None, oaurl=None, track=None, date=None, latlims=None, lonlims=None, verbose=False):
        if (beam is None) or ((oaurl is None) and (None in [track, date, latlims, lonlims])):
            raise Exception('''Please specify a beam and 
            - either: an OpenAltimetry API url, 
            - or: a track, date, latitude limits and longitude limits.''')
        else:
            if oaurl is not None:
                url = oaurl
                tofind = '&beamName='
                ids = url.find(tofind)
                while ids>-1:
                    url = url.replace(url[ids:ids+len(tofind)+4],'')
                    ids = url.find(tofind)
                iprod = url.find('/atl')
                url = url.replace(url[iprod:iprod+6],'/atlXX')
                url += tofind + beam + '&client=jupyter'

                idate = url.find('date=') + len('date=')
                date = url[idate:idate+10]
                itrack = url.find('trackId=') + len('trackId=')
                trackend = url[itrack:].find('&')
                track = int(url[itrack:itrack+trackend])
                bb = []
                for s in ['minx=', 'maxx=', 'miny=', 'maxy=']:
                    ids = url.find(s) + len(s)
                    ide = url[ids:].find('&')
                    bb.append(float(url[ids:ids+ide]))
                lonlims = bb[:2]
                latlims = bb[2:]
            elif None not in [track, date, latlims, lonlims]:
                url = 'https://openaltimetry.org/data/api/icesat2/atlXX?'
                url += 'date={date}&minx={minx}&miny={miny}&maxx={maxx}&maxy={maxy}&trackId={track}&beamName={beam}'.format(
                        date=date,minx=lonlims[0],miny=latlims[0],maxx=lonlims[1],maxy=latlims[1],track=track,beam=beam)
                url += '&outputFormat=json&client=jupyter'
            
            self.url = url
            self.date = date
            self.track = track
            self.beam = beam
            self.latlims = latlims
            self.lonlims = lonlims
            if verbose:
                print('OpenAltimetry API URL:', self.url)
                print('Date:', self.date)
                print('Track:', self.track)
                print('Beam:', self.beam)
                print('Latitude limits:', self.latlims)
                print('Longitude limits:', self.lonlims)
                
                
    ################################################################################################ 
    def requestData(self, verbose=False): 
        if verbose:
            print('---> requesting ATL03 data...',end='')
        product = 'atl03'
        request_url = self.url.replace('atlXX',product)
        data = requests.get(request_url).json()
        lat, lon, h, confs = [], [], [], []
        for beam in data:
            for confidence in beam['series']:
                for p in confidence['data']:
                    confs.append(confidence['name'])
                    lat.append(p[0])
                    lon.append(p[1])
                    h.append(p[2])
        self.atl03 = pd.DataFrame(list(zip(lat,lon,h,confs)), columns = ['lat','lon','h','conf'])
        if verbose:
            if len(self.atl03)>0: print(' %i data points.' % len(self.atl03))
            else: print(' No data.')
            
            print('---> requesting ATL06 data...',end='')
        product = 'atl06'
        request_url = self.url.replace('atlXX',product)
        data = requests.get(request_url).json()
        self.atl06 = pd.DataFrame(data['series'][0]['lat_lon_elev'], columns = ['lat','lon','h'])
        if verbose:
            if len(self.atl06)>0: print(' %i data points.' % len(self.atl06)) 
            else: print(' No data.')
            
            print('---> requesting ATL07 data...',end='')
        product = 'atl07'
        request_url = self.url.replace('atlXX',product)
        data = requests.get(request_url).json()
        self.atl07 = pd.DataFrame(data['series'][0]['lat_lon_elev'], columns = ['lat','lon','h'])
        if verbose:
            if len(self.atl07)>0: print(' %i data points.' % len(self.atl07)) 
            else: print(' No data.')
            
            print('---> requesting ATL08 data...',end='')
        product = 'atl08'
        request_url = self.url.replace('atlXX',product)
        data = requests.get(request_url).json()
        self.atl08 = pd.DataFrame(data['series'][0]['lat_lon_elev_canopy'], columns = ['lat','lon','h','canopy'])
        if verbose:
            if len(self.atl08)>0: print(' %i data points.' % len(self.atl08)) 
            else: print(' No data.')
            
            print('---> requesting ATL10 data...',end='')
        product = 'atl10'
        request_url = self.url.replace('atlXX',product)
        data = requests.get(request_url).json()
        self.atl10 = pd.DataFrame(data['series'][0]['lat_lon_elev'], columns = ['lat','lon','h'])
        if verbose:
            if len(self.atl10)>0: print(' %i data points.' % len(self.atl10)) 
            else: print(' No data.')
            
            print('---> requesting ATL12 data...',end='')
        product = 'atl12'
        request_url = self.url.replace('atlXX',product)
        data = requests.get(request_url).json()
        self.atl12 = pd.DataFrame(data['series'][0]['lat_lon_elev'], columns = ['lat','lon','h'])
        if verbose:
            if len(self.atl12)>0: print(' %i data points.' % len(self.atl12)) 
            else: print(' No data.')
            
            print('---> requesting ATL13 data...',end='')
        product = 'atl13'
        request_url = self.url.replace('atlXX',product)
        data = requests.get(request_url).json()
        self.atl13 = pd.DataFrame(data['series'][0]['lat_lon_elev'], columns = ['lat','lon','h'])
        if verbose:
            if len(self.atl13)>0: print(' %i data points.' % len(self.atl13)) 
            else: print(' No data.')
    
    
    ################################################################################################ 
    def plotData(self,ax=None,title='some cool ICESat-2 data I found on OpenAltimetry'):

        # get data if not already there
        if 'atl03' not in vars(self).keys(): 
            print('Data has not yet been requested from OpenAltimetry yet. Doing this now.')
            self.requestData(verbose=True)

        axes_not_specified = True if ax == None else False

        # create the figure and axis
        if axes_not_specified:
            fig, ax = plt.subplots(figsize=[8,5])
            
        if len(self.atl03)>0:
            atl03 = ax.scatter(self.atl03.lat, self.atl03.h, s=2, color='black', alpha=0.2, label='ATL03')
        if len(self.atl06)>0:
            atl06, = ax.plot(self.atl06.lat, self.atl06.h, c='C0', linestyle='-', label='ATL06')
        if len(self.atl07)>0:   
            atl07, = ax.plot(self.atl07.lat, self.atl07.h, c='C1', linestyle='--', label='ATL07')
        if len(self.atl08)>0:   
            atl08, = ax.plot(self.atl08.lat, self.atl08.h, c='C2', linestyle=':', label='ATL08')
        try:
            if np.sum(~np.isnan(self.atl08.canopy))>0:
                atl08canopy = ax.scatter(self.atl08.lat, self.atl08.h+self.atl08.canopy, s=2, c='C2', label='ATL08 canopy')
        except: 
            print('could not display ATL08 canopy data')
        if len(self.atl10)>0:   
            atl08, = ax.plot(self.atl10.lat, self.atl10.h, c='C3', linestyle='-', label='ATL10')
        if len(self.atl12)>0:   
            atl12, = ax.plot(self.atl12.lat, self.atl12.h, c='C4', linestyle='--', label='ATL12')
        if len(self.atl13)>0:   
            atl13, = ax.plot(self.atl13.lat, self.atl13.h, c='C5', linestyle=':', label='ATL13')

        heights = self.atl03.h[self.atl03.conf != 'Noise']
        y_min1 = np.min(heights)
        y_max1 = np.max(heights)
        maxprods = np.nanmax((self.atl06.h.max(), self.atl07.h.max(), self.atl08.h.max(), 
                              self.atl10.h.max(), self.atl12.h.max(), self.atl13.h.max()))
        minprods = np.nanmin((self.atl06.h.min(), self.atl07.h.min(), self.atl08.h.min(), 
                              self.atl10.h.min(), self.atl12.h.min(), self.atl13.h.min()))
        hrange = maxprods - minprods
        y_min2 = minprods - hrange * 0.5
        y_max2 = maxprods + hrange * 0.5
        y_min = np.nanmin((y_min1, y_min2))
        y_max = np.nanmax((y_max1, y_max2))

        x_min = self.atl03.lat.min()
        x_max = self.atl03.lat.max()

        ax.set_xlim((x_min, x_max))
        ax.set_ylim((y_min, y_max))

        # label the axes
        ax.set_title(title)
        ax.set_xlabel('latitude')
        ax.set_ylabel('elevation in meters')

        # add a legend
        ax.legend(loc='upper right')

        # add some text to provide info on what is plotted
        info = 'ICESat-2 track {track:d}-{beam:s} on {date:s} ({lon:.4f}E, {lat:.4f}N)'.format(track=self.track, 
                                                                                                beam=self.beam, 
                                                                                                date=self.date, 
                                                                                                lon=np.mean(self.lonlims), 
                                                                                                lat=np.mean(self.latlims))
        infotext = ax.text(0.02, 0.97, info,
                           horizontalalignment='left', 
                           verticalalignment='top', 
                           transform=ax.transAxes,
                           fontsize=7,
                           bbox=dict(edgecolor=None, facecolor='white', alpha=0.9, linewidth=0))

        if axes_not_specified:
            fig.tight_layout()
            return fig
        else:
            return ax

    def visualize_sentinel2(self, max_cloud_prob=20, days_buffer=10, gamma_value=1.8, 
                            title='ICESat-2 data', imagery_filename='my-satellite-image.tif', plot_filename='my-plot.jpg'):

        # request data, if not already done so
        if 'atl03' not in vars(self).keys():
            print('--> Getting data from OpenAltimetry.')
            self.requestData(verbose=True)
            
        ######################
        # get the ground track from the available higher-level products
        diff = 0
        if len(self.atl06 > 1):
            diff = self.atl06.lat.iloc[-1] - self.atl06.lat.iloc[0]
        elif len(self.atl08 > 1):
            diff = self.atl08.lat.iloc[-1] - self.atl08.lat.iloc[0]
        elif len(self.atl12 > 1):
            diff = self.atl12.lat.iloc[-1] - self.atl12.lat.iloc[0]
        elif len(self.atl07 > 1):
            diff = self.atl07.lat.iloc[-1] - self.atl07.lat.iloc[0]
        elif len(self.atl10 > 1):
            diff = self.atl10.lat.iloc[-1] - self.atl10.lat.iloc[0]
        elif len(self.atl13 > 1):
            diff = self.atl13.lat.iloc[-1] - self.atl13.lat.iloc[0]
        ascending = True if diff>=0 else False
        vs = ['lat', 'lon']
        gtlatlon = pd.concat((self.atl06[vs], 
                               self.atl07[vs],
                               self.atl08[vs],
                               self.atl10[vs],
                               self.atl12[vs],
                               self.atl13[vs])).sort_values(by='lat').groupby('lat').mean().reset_index()
        n_pts_gt = 500
        lat_interp = np.linspace(gtlatlon.lat.min(), gtlatlon.lat.max(), n_pts_gt)
        lon_interp = np.interp(lat_interp, gtlatlon.lat, gtlatlon.lon)
        gt = pd.DataFrame({'lat': lat_interp, 'lon': lon_interp}).sort_values(by='lat', ascending=ascending).reset_index()
        
        ######################
        # get ground track stats
        def dist_latlon2meters(lat1, lon1, lat2, lon2):
            # returns the distance between two coordinate points - (lon1, lat1) and (lon2, lat2) along the earth's surface in meters.
            R = 6371000
            def deg2rad(deg):
                return deg * (np.pi/180)
            dlat = deg2rad(lat2-lat1)
            dlon = deg2rad(lon2-lon1)
            a = np.sin(dlat/2) * np.sin(dlat/2) + np.cos(deg2rad(lat1)) * np.cos(deg2rad(lat2)) * np.sin(dlon/2) * np.sin(dlon/2)
            c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1-a))
            return R * c

        lat1, lat2 = gt.lat.iloc[0], gt.lat.iloc[-1]
        lon1, lon2 = gt.lon.iloc[0], gt.lon.iloc[-1]
        center_lon = (lon1 + lon2) / 2
        center_lat = (lat1 + lat2) / 2
        ground_track_length = dist_latlon2meters(lat1, lon1, lat2, lon2)
        print('The ground track is %.1f km long.' % (ground_track_length/1e3))

        # get along-track distance
        gt['xatc'] = np.linspace(0, ground_track_length, n_pts_gt)
        self.gt = gt
    
        ######################
        # define a function for getting Sentinel-2 collection with s2cloudless probabilities and adding along-track mean cloud probability
        def get_sentinel2_cloud_collection(mydata, days_buffer=days_buffer, gt_buffer=100, CLD_PRB_THRESH=40, BUFFER=100):
            # create the area of interest for cloud likelihood assessment
            ground_track_coordinates = list(zip(mydata.gt.lon, mydata.gt.lat))
            ground_track_projection = 'EPSG:4326' # our data is lon/lat in degrees [https://epsg.io/4326]
            gtx_feature = ee.Geometry.LineString(coords=ground_track_coordinates,
                                             proj=ground_track_projection,
                                             geodesic=True)
            area_of_interest = gtx_feature.buffer(gt_buffer)

            datetime_requested = datetime.strptime(mydata.date, '%Y-%m-%d')
            start_date = (datetime_requested - timedelta(days=days_buffer, hours=-12)).strftime('%Y-%m-%dT%H:%M:%S')
            end_date = (datetime_requested + timedelta(days=days_buffer, hours=12)).strftime('%Y-%m-%dT%H:%M:%S')
            print('Looking for Sentinel-2 images from %s to %s' % (start_date, end_date), end=' ')

            # Import and filter S2 SR HARMONIZED
            s2_sr_collection = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
                .filterBounds(area_of_interest)
                .filterDate(start_date, end_date))

            # Import and filter s2cloudless.
            s2_cloudless_collection = (ee.ImageCollection('COPERNICUS/S2_CLOUD_PROBABILITY')
                .filterBounds(area_of_interest)
                .filterDate(start_date, end_date))

            # Join the filtered s2cloudless collection to the SR collection by the 'system:index' property.
            cloud_collection = ee.ImageCollection(ee.Join.saveFirst('s2cloudless').apply(**{
                'primary': s2_sr_collection,
                'secondary': s2_cloudless_collection,
                'condition': ee.Filter.equals(**{
                    'leftField': 'system:index',
                    'rightField': 'system:index'
                })
            }))

            cloud_collection = cloud_collection.map(lambda img: img.addBands(ee.Image(img.get('s2cloudless')).select('probability')))
            
# THE CODE COMMENTED OUT HERE WOULD ACTUALLY CREATE A CLOUD MASK AND APPLY IT, BUT THIS SEEMS TO RUN FOR REALLY LONG...
#             def add_cloud_bands(img):
#                 # Get s2cloudless image, subset the probability band.
#                 cld_prb = ee.Image(img.get('s2cloudless')).select('probability')

#                 # Condition s2cloudless by the probability threshold value.
#                 is_cloud = cld_prb.gt(CLD_PRB_THRESH).rename('clouds')

#                 # Add the cloud probability layer and cloud mask as image bands.
#                 return img.addBands(ee.Image([cld_prb, is_cloud]))
            
#             def add_cloud_mask(img): 
#                 # Combine cloud and shadow mask, set cloud and shadow as value 1, else 0.
#                 is_cld_shdw = img.select('clouds').gt(0)

#                 # Remove small cloud-shadow patches and dilate remaining pixels by BUFFER input.
#                 # 20 m scale is for speed, and assumes clouds don't require 10 m precision.
#                 is_cld_shdw = (is_cld_shdw.focalMin(2).focalMax(BUFFER*2/20)
#                     .reproject(**{'crs': img.select([0]).projection(), 'scale': 20})
#                     .rename('cloudmask'))
            
#                 return img.addBands(is_cld_shdw)
            
#             cloud_collection = cloud_collection.map(add_cloud_bands).map(add_cloud_mask)

            def set_is2_cloudiness(img, aoi=area_of_interest):
                cloudprob = img.select(['probability']).reduceRegion(reducer=ee.Reducer.mean(), 
                                                                     geometry=aoi, 
                                                                     bestEffort=True, 
                                                                     maxPixels=1e6)
                return img.set('ground_track_cloud_prob', cloudprob.get('probability'))

            cloud_collection = cloud_collection.map(set_is2_cloudiness)
            
#             def apply_cld_shdw_mask(img):
#                 # Subset the cloudmask band and invert it so clouds/shadow are 0, else 1.
#                 not_cld_shdw = img.select('cloudmask').Not()

#                 # Subset reflectance bands and update their masks, return the result.
#                 return img.select('B.*').updateMask(not_cld_shdw)
            
#             cloud_collection = cloud_collection.map(apply_cld_shdw_mask)
            
            return cloud_collection
        
        ######################
        # get the Sentinel-2 collection with s2cloudless and along-track mean cloud probability
        # if there's no results keep expanding the days_buffer until at least one image is found, or 
        collection_size = 0
        if days_buffer > 200:
            days_buffer = 200
        increment_days = days_buffer
        while (collection_size<10) & (days_buffer <= 200):

            collection = get_sentinel2_cloud_collection(self, days_buffer=days_buffer)

            # filter collection to only images that are (mostly) cloud-free along the ICESat-2 ground track
            cloudfree_collection = collection.filter(ee.Filter.lt('ground_track_cloud_prob', max_cloud_prob))

            collection_size = cloudfree_collection.size().getInfo()
            if collection_size == 1: 
                print('--> there is %i cloud-free image.' % collection_size)
            elif collection_size > 1: 
                print('--> there are %i cloud-free images.' % collection_size)
            else:
                print('--> there are not enough cloud-free images: widening date range...')
            days_buffer += increment_days

        # get the time difference between ICESat-2 and Sentinel-2 and sort by it 
        is2time = self.date + 'T12:00:00'
        def set_time_difference(img, is2time=is2time):
            timediff = ee.Date(is2time).difference(img.get('system:time_start'), 'second').abs()
            return img.set('timediff', timediff)
        cloudfree_collection = cloudfree_collection.map(set_time_difference).sort('timediff')

        # create a region around the ground track over which to download data
        point_of_interest = ee.Geometry.Point(center_lon, center_lat)
        buffer_around_center_meters = ground_track_length*0.52
        region_of_interest = point_of_interest.buffer(buffer_around_center_meters)
        
        ######################
        # select the first image, and turn it into an 8-bit RGB for download
        selectedImage = cloudfree_collection.first()
        mosaic = cloudfree_collection.sort('timediff', False).mosaic()
        rgb = mosaic.select('B4', 'B3', 'B2')
        # rgbmax = rgb.reduce(ee.Reducer.max()).reduceRegion(reducer=ee.Reducer.max(), geometry=region_of_interest, bestEffort=True, maxPixels=1e6)
        # rgbmin = rgb.reduce(ee.Reducer.min()).reduceRegion(reducer=ee.Reducer.min(), geometry=region_of_interest, bestEffort=True, maxPixels=1e6)
        # rgb = rgb.unitScale(ee.Number(rgbmin.get('min')), ee.Number(rgbmax.get('max'))).clamp(0.0, 1.0)
        rgb = rgb.unitScale(0, 10000).clamp(0.0, 1.0)
        rgb_gamma = rgb.pow(1/gamma_value)
        rgb8bit= rgb_gamma.multiply(255).uint8()

        ######################
        # from the selected image get some stats: product id, cloud probability and time difference from icesat-2
        prod_id = selectedImage.get('PRODUCT_ID').getInfo()
        cld_prb = selectedImage.get('ground_track_cloud_prob').getInfo()
        s2datetime = datetime.fromtimestamp(selectedImage.get('system:time_start').getInfo()/1e3)
        s2datestr = datetime.strftime(s2datetime, '%Y-%b-%d')
        is2datetime = datetime.strptime(self.date, '%Y-%m-%d') + timedelta(hours=12)
        timediff = s2datetime - is2datetime
        days_diff = (timediff + timedelta(hours=12)).days
        if days_diff == 0: diff_str = 'Same day as'
        if days_diff == 1: diff_str = '1 day after'
        if days_diff == -1: diff_str = '1 day before'
        if days_diff > 1: diff_str = '%i days after' % np.abs(days_diff)
        if days_diff < -1: diff_str = '%i days before' % np.abs(days_diff)

        print('--> Closest cloud-free Sentinel-2 image to ICESat:')
        print('    - product_id: %s' % prod_id)
        print('    - time difference: %s ICESat-2' % diff_str)
        print('    - mean along-track cloud probability: %.1f' % cld_prb)
        
        ######################
        # get the download URL and download the selected image
        success = False
        scale = 10
        tries = 0
        while (success == False) & (tries <= 5):
            try:
                downloadURL = rgb8bit.getDownloadUrl({'name': 'mySatelliteImage',
                                                          'crs': selectedImage.select('B3').projection().crs(),
                                                          'scale': scale,
                                                          'region': region_of_interest,
                                                          'filePerBand': False,
                                                          'format': 'GEO_TIFF'})

                response = requests.get(downloadURL)
                with open(imagery_filename, 'wb') as f:
                    f.write(response.content)

                print('--> Downloaded the 8-bit RGB image as %s.' % imagery_filename)
                success = True
                tries += 1
            except:
                # traceback.print_exc()
                scale *= 2
                print('-> download unsuccessful, increasing scale to %.1f...' % scale)
                success = False
                tries += 1
            
        myImage = rio.open(imagery_filename)
        
        ######################
        # make the figure
        fig = plt.figure(figsize=[10,4.5])
        gs = fig.add_gridspec(1, 5)
        ax1 = fig.add_subplot(gs[0, 0:2])
        ax2 = fig.add_subplot(gs[0, 2:])

        ######################
        # plot the imagery
        ax = ax1
        rioplot.show(myImage, ax=ax)
        ximg, yimg = warp.transform(src_crs='epsg:4326', dst_crs=myImage.crs, xs=self.gt.lon, ys=self.gt.lat)
        ax.annotate('', xy=(ximg[-1], yimg[-1]), xytext=(ximg[0], yimg[0]),
                     arrowprops=dict(width=0.7, headwidth=5, headlength=5, color='r'),zorder=1000)
        ax.axis('off')

        add_graticule(img=myImage, ax_img=ax)

        # add some info about the Sentinel-2 image
        txt = 'Sentinel-2 on %s\n' % s2datestr
        txt += '%s\n' % prod_id
        txt += '- time difference: %s ICESat-2\n' % diff_str
        txt += '- mean along-track cloud probability: %.1f%%' % cld_prb
        ax1.text(0.0, -0.01, txt, transform=ax1.transAxes, ha='left', va='top',fontsize=6)

        ######################
        # plot the ICESat-2 data
        ax = ax2 
        self.plotData(ax=ax, title=title)

        # adjust font sizes
        ax.tick_params(labelsize=7)
        ax.yaxis.label.set_size(8)
        ax.set_xlabel('')
        ax.legend(loc='upper right',fontsize=8)
        # flip x-axis if track is descending, to make along-track distance go from left to right
        if gt.lat.iloc[0] > gt.lat.iloc[-1]:
            ax.set_xlim(np.flip(np.array(ax.get_xlim())))

        # add along-track distance
        lx = self.gt.sort_values(by='xatc').iloc[[0,-1]][['xatc','lat']].reset_index(drop=True)
        lat = np.array(lx.lat)
        xatc = np.array(lx.xatc) / 1e3
        def lat2xatc(l):
            return xatc[0] + (l - lat[0]) * (xatc[1] - xatc[0]) /(lat[1] - lat[0])
        def xatc2lat(x):
            return lat[0] + (x - xatc[0]) * (lat[1] - lat[0]) / (xatc[1] - xatc[0])
        secax = ax.secondary_xaxis(-0.075, functions=(lat2xatc, xatc2lat))
        secax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
        secax.set_xlabel('latitude / along-track distance (km)',fontsize=8,labelpad=0)
        secax.tick_params(axis='both', which='major', labelsize=7)
        secax.ticklabel_format(useOffset=False) # show actual readable latitude values

        fig.tight_layout()
        
        fig.savefig(plot_filename, dpi=600)
        print('--> Saved plot as %s.' % plot_filename)
        
        return fig


################################################################################################ 
def add_graticule(img, ax_img):
    from utils.curve_intersect import intersection
    latlon_bbox = warp.transform(img.crs, {'init': 'epsg:4326'}, 
                                 [img.bounds[i] for i in [0,2,2,0,0]], 
                                 [img.bounds[i] for i in [1,1,3,3,1]])
    min_lat = np.min(latlon_bbox[1])
    max_lat = np.max(latlon_bbox[1])
    min_lon = np.min(latlon_bbox[0])
    max_lon = np.max(latlon_bbox[0])
    latdiff = max_lat-min_lat
    londiff = max_lon-min_lon
    diffs = np.array([0.0001, 0.0002, 0.00025, 0.0004, 0.0005,
                      0.001, 0.002, 0.0025, 0.004, 0.005, 
                      0.01, 0.02, 0.025, 0.04, 0.05, 0.1, 0.2, 0.25, 0.4, 0.5, 1, 2])
    latstep = np.min(diffs[diffs>latdiff/8])
    lonstep = np.min(diffs[diffs>londiff/8])
    minlat = np.floor(min_lat/latstep)*latstep
    maxlat = np.ceil(max_lat/latstep)*latstep
    minlon = np.floor(min_lon/lonstep)*lonstep
    maxlon = np.ceil(max_lon/lonstep)*lonstep

    # plot meridians and parallels
    xl = (img.bounds.left, img.bounds.right)
    yl = (img.bounds.bottom, img.bounds.top)
    meridians = np.arange(minlon,maxlon, step=lonstep)
    parallels = np.arange(minlat,maxlat, step=latstep)
    latseq = np.linspace(minlat,maxlat,200)
    lonseq = np.linspace(minlon,maxlon,200)
    gridcol = 'k'
    gridls = ':'
    gridlw = 0.5
    topline = [[xl[0],xl[1]],[yl[1],yl[1]]]
    bottomline = [[xl[0],xl[1]],[yl[0],yl[0]]]
    leftline = [[xl[0],xl[0]],[yl[0],yl[1]]]
    rightline = [[xl[1],xl[1]],[yl[0],yl[1]]]
    for me in meridians:
        gr_trans = warp.transform({'init': 'epsg:4326'},img.crs,me*np.ones_like(latseq),latseq)
        deglab = ' %.10g°E' % me if me >= 0 else ' %.10g°W' % -me
        intx,inty = intersection(topline[0], topline[1], gr_trans[0], gr_trans[1])
        if len(intx) > 0:
            intx = intx[0]
            inty = inty[0]
            ax_img.text(intx, inty, deglab, fontsize=6, color='gray',verticalalignment='bottom',horizontalalignment='center',
                    rotation='vertical')
        thislw = gridlw
        ax_img.plot(gr_trans[0],gr_trans[1],c=gridcol,ls=gridls,lw=thislw,alpha=0.5)
    for pa in parallels:
        gr_trans = warp.transform({'init': 'epsg:4326'},img.crs,lonseq,pa*np.ones_like(lonseq))
        thislw = gridlw
        deglab = ' %.10g°N' % pa if pa >= 0 else ' %.10g°S' % -pa
        intx,inty = intersection(rightline[0], rightline[1], gr_trans[0], gr_trans[1])
        if len(intx) > 0:
            intx = intx[0]
            inty = inty[0]
            ax_img.text(intx, inty, deglab, fontsize=6, color='gray',verticalalignment='center',horizontalalignment='left')
        ax_img.plot(gr_trans[0],gr_trans[1],c=gridcol,ls=gridls,lw=thislw,alpha=0.5)
        ax_img.set_xlim(xl)
        ax_img.set_ylim(yl)