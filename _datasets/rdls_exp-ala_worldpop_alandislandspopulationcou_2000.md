---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-aland-islands
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-aland-islands
dataset_id: rdls_exp-ala_worldpop_alandislandspopulationcou_2000
description: 'WorldPop produces different types of gridded population count datasets,
  depending on the methods used and end application. Please make sure you have read
  our Mapping Populations overview page before choosing and downloading a dataset.
  Bespoke methods used to produce datasets for specific individual countries are available
  through the WorldPop Open Population Repository (WOPR) link below. These are 100m
  resolution gridded population estimates using customized methods ('' bottom-up ''
  and/or '' top-down '') developed for the latest data available from each country.
  They can also be visualised and explored through the woprVision App . The remaining
  datasets in the links below are produced using the '' top-down '' method, with either
  the unconstrained or constrained top-down disaggregation method used. Please make
  sure you read the Top-down estimation modelling overview page to decide on which
  datasets best meet your needs. Datasets are available to download in Geotiff and
  ASCII XYZ format at a resolution of 3 and 30 arc-seconds (approximately 100m and
  1km at the equator, respectively): - Unconstrained individual countries 2000-2020
  ( 1km resolution ): Consistent 1km resolution population count datasets created
  using unconstrained top-down methods for all countries of the World for each year
  2000-2020. - Unconstrained individual countries 2000-2020 ( 100m resolution ): Consistent
  100m resolution population count datasets created using unconstrained top-down methods
  for all countries of the World for each year 2000-2020. - Unconstrained individual
  countries 2000-2020 UN adjusted ( 100m resolution ): Consistent 100m resolution
  population count datasets created using unconstrained top-down methods for all countries
  of the World for each year 2000-2020 and adjusted to match United Nations national
  population estimates (UN 2019) -Unconstrained individual countries 2000-2020 UN
  adjusted ( 1km resolution ): Consistent 1km resolution population count datasets
  created using unconstrained top-down methods for all countries of the World for
  each year 2000-2020 and adjusted to match United Nations national population estimates
  (UN 2019). -Unconstrained global mosaics 2000-2020 ( 1km resolution ): Mosaiced
  1km resolution versions of the ''Unconstrained individual countries 2000-2020''
  datasets. -Constrained individual countries 2020 ( 100m resolution ): Consistent
  100m resolution population count datasets created using constrained top-down methods
  for all countries of the World for 2020. -Constrained individual countries 2020
  UN adjusted ( 100m resolution ): Consistent 100m resolution population count datasets
  created using constrained top-down methods for all countries of the World for 2020
  and adjusted to match United Nations national population estimates (UN 2019). Older
  datasets produced for specific individual countries and continents, using a set
  of tailored geospatial inputs and differing ''top-down'' methods and time periods
  are still available for download here: Individual countries and Whole Continent
  . Data for earlier dates is available directly from WorldPop. WorldPop (www.worldpop.org
  - School of Geography and Environmental Science, University of Southampton; Department
  of Geography and Geosciences, University of Louisville; Departement de Geographie,
  Universite de Namur) and Center for International Earth Science Information Network
  (CIESIN), Columbia University (2018). Global High Resolution Population Denominators
  Project - Funded by The Bill and Melinda Gates Foundation (OPP1134076). https://dx.doi.org/10.5258/SOTON/WP00645.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-for-aland-islands]'
details: null
exposure:
- asset_type:
    description: "Gridded population counts at 100m resolution using dasymetric redistribution\
      \ methods for \xC5land Islands"
    id: population
    scheme: null
    title: null
    uri: null
  category: population
  id: exposure_1
  metrics:
  - dimension: population
    id: metric_1
    measurement:
      quantity_kind: count
      unit: count
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: "WorldPop produced gridded population estimates for \xC5land Islands\
    \ using dasymetric redistribution methods applied to census and ancillary geospatial\
    \ data, generating 100m resolution raster datasets of population counts per grid\
    \ cell in GeoTIFF format for multiple years (2016-2020)."
  sources:
  - id: source_1
    license: null
    name: WorldPop
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/worldpop-population-counts-for-aland-islands
  rel: source
loss:
  losses: []
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://doi.org/10.1371/journal.pone.0107042-
- author_names: null
  date_published: null
  doi: null
  id: reference_2
  name: Methodology documentation
  url: https://doi.org/10.1016/j.compenvurbsys.2019.101444-
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: https://dx.doi.org/10.5258/SOTON/WP00665
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2020, \xC5land Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/ALA/ala_ppp_2020.tif
  format: null
  id: resource_cf4cb383
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2019, \xC5land Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/ALA/ala_ppp_2019.tif
  format: null
  id: resource_eb422484
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2018, \xC5land Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/ALA/ala_ppp_2018.tif
  format: null
  id: resource_0c0adc14
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2017, \xC5land Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/ALA/ala_ppp_2017.tif
  format: null
  id: resource_df83a378
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2016, \xC5land Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/ALA/ala_ppp_2016.tif
  format: null
  id: resource_5f4a6e8b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2020, Aland Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/ALA/ala_ppp_2020_constrained.tif
  format: null
  id: resource_202bcb0d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2020_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2020 Aland Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/ALA/ala_ppp_2020_1km_Aggregated.tif
  format: null
  id: resource_a0ca975d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2020_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2020 Aland Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/ALA/ala_ppp_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_986481b7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2019 Aland Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/ALA/ala_ppp_2019_1km_Aggregated.tif
  format: null
  id: resource_1c92d21a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2019_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2019 Aland Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/ALA/ala_ppp_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_9689efcb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2018 Aland Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/ALA/ala_ppp_2018_1km_Aggregated.tif
  format: null
  id: resource_af2260ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2018_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2018 Aland Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/ALA/ala_ppp_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_3eaada2c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2017 Aland Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/ALA/ala_ppp_2017_1km_Aggregated.tif
  format: null
  id: resource_e00023c0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2017_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2017 Aland Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/ALA/ala_ppp_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_23250e58
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2016 Aland Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/ALA/ala_ppp_2016_1km_Aggregated.tif
  format: null
  id: resource_e4b026df
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2016_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "\xC5land Islands - Population Counts (The spatial distribution of\
    \ population in 2016 Aland Islands)"
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/ALA/ala_ppp_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_0e896c84
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: ala_ppp_2016_1km_ASCII_XYZ.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-ala_worldpop_alandislandspopulationcou_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - ALA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: "\xC5land Islands - Population Counts"
version: null
vulnerability: null
---
