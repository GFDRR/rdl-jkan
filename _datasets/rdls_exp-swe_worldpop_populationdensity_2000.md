---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-density-for-sweden
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-density-for-sweden
dataset_id: rdls_exp-swe_worldpop_populationdensity_2000
description: 'WorldPop produces different types of gridded population count datasets,
  depending on the methods used and end application. Please make sure you have read
  our Mapping Populations overview page before choosing and downloading a dataset.
  Datasets are available to download in Geotiff and ASCII XYZ format at a resolution
  of 30 arc-seconds (approximately 1km at the equator) -Unconstrained individual countries
  2000-2020: Population density datasets for all countries of the World for each year
  2000-2020 - derived from the corresponding Unconstrained individual countries 2000-2020
  population count datasets by dividing the number of people in each pixel by the
  pixel surface area. These are produced using the unconstrained top-down modelling
  method . -Unconstrained individual countries 2000-2020 UN adjusted: Population density
  datasets for all countries of the World for each year 2000-2020 - derived from the
  corresponding Unconstrained individual countries 2000-2020 population UN adjusted
  count datasets by dividing the number of people in each pixel, adjusted to match
  the country total from the official United Nations population estimates (UN 2019),
  by the pixel surface area. These are produced using the unconstrained top-down modelling
  method . Data for earlier dates is available directly from WorldPop. WorldPop (www.worldpop.org
  - School of Geography and Environmental Science, University of Southampton; Department
  of Geography and Geosciences, University of Louisville; Departement de Geographie,
  Universite de Namur) and Center for International Earth Science Information Network
  (CIESIN), Columbia University (2018). Global High Resolution Population Denominators
  Project - Funded by The Bill and Melinda Gates Foundation (OPP1134076). https://dx.doi.org/10.5258/SOTON/WP00674.
  [Source: This metadata record was automatically extracted from the Humanitarian
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-density-for-sweden]'
details: null
exposure:
- asset_type:
    description: Gridded population density estimates at 1km resolution for Sweden,
      2016-2020
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
      quantity_kind: area
      unit: null
hazard: null
license: https://creativecommons.org/licenses/by/4.0/
lineage:
  description: WorldPop population density estimates derived from census data and
    geospatial modeling techniques, gridded at 30 arc-second (approximately 1km) resolution
    in WGS84 projection. Data available in both UN-adjusted and unadjusted variants
    for years 2016-2020, expressed as people per square kilometer.
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
- href: https://data.humdata.org/dataset/worldpop-population-density-for-sweden
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sweden - Population Density (The spatial distribution of population
    density in 2020, Sweden)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2020/SWE/swe_pd_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_cf927466
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sweden - Population Density (The spatial distribution of population
    density in 2020, Sweden)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2020/SWE/swe_pd_2020_1km.tif
  format: null
  id: resource_a2bb98fa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2020_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2020 based on country
    total adjusted to match the corresponding UNPD estimate, Sweden
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2020/SWE/swe_pd_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_dbc7013c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2020 based on country
    total adjusted to match the corresponding UNPD estimate, Sweden
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2020/SWE/swe_pd_2020_1km_UNadj.tif
  format: null
  id: resource_85bf7f17
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2020_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sweden - Population Density (The spatial distribution of population
    density in 2019, Sweden)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2019/SWE/swe_pd_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_f439407d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sweden - Population Density (The spatial distribution of population
    density in 2019, Sweden)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2019/SWE/swe_pd_2019_1km.tif
  format: null
  id: resource_f68c4b47
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2019_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2019 based on country
    total adjusted to match the corresponding UNPD estimate, Sweden
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2019/SWE/swe_pd_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_565e590a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2019 based on country
    total adjusted to match the corresponding UNPD estimate, Sweden
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2019/SWE/swe_pd_2019_1km_UNadj.tif
  format: null
  id: resource_48177dee
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2019_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sweden - Population Density (The spatial distribution of population
    density in 2018, Sweden)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2018/SWE/swe_pd_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_b0f78100
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sweden - Population Density (The spatial distribution of population
    density in 2018, Sweden)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2018/SWE/swe_pd_2018_1km.tif
  format: null
  id: resource_5899aa3a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2018_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2018 based on country
    total adjusted to match the corresponding UNPD estimate, Sweden
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2018/SWE/swe_pd_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_01f42143
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2018 based on country
    total adjusted to match the corresponding UNPD estimate, Sweden
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2018/SWE/swe_pd_2018_1km_UNadj.tif
  format: null
  id: resource_4bac1dc1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2018_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sweden - Population Density (The spatial distribution of population
    density in 2017, Sweden)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2017/SWE/swe_pd_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_ba9114ca
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sweden - Population Density (The spatial distribution of population
    density in 2017, Sweden)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2017/SWE/swe_pd_2017_1km.tif
  format: null
  id: resource_c2c435fc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2017_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2017 based on country
    total adjusted to match the corresponding UNPD estimate, Sweden
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2017/SWE/swe_pd_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_336a3a1c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2017 based on country
    total adjusted to match the corresponding UNPD estimate, Sweden
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2017/SWE/swe_pd_2017_1km_UNadj.tif
  format: null
  id: resource_f559738f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2017_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sweden - Population Density (The spatial distribution of population
    density in 2016, Sweden)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2016/SWE/swe_pd_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_ca17e45c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Sweden - Population Density (The spatial distribution of population
    density in 2016, Sweden)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2016/SWE/swe_pd_2016_1km.tif
  format: null
  id: resource_f9c684ed
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2016_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2016 based on country
    total adjusted to match the corresponding UNPD estimate, Sweden
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2016/SWE/swe_pd_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_09de04e8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2016 based on country
    total adjusted to match the corresponding UNPD estimate, Sweden
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2016/SWE/swe_pd_2016_1km_UNadj.tif
  format: null
  id: resource_52c2d1f4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swe_pd_2016_1km_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-swe_worldpop_populationdensity_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - SWE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Sweden - Population Density
version: null
vulnerability: null
---
