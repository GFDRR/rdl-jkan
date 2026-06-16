---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-density-for-ghana
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-density-for-ghana
dataset_id: rdls_exp-gha_worldpop_populationdensity_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-density-for-ghana]'
details: null
exposure:
- asset_type:
    description: Gridded population density estimates at 1km resolution for Ghana,
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
    geospatial modeling at 30 arc-second (approximately 1km) resolution. Data available
    in both UN-adjusted and unadjusted variants in GeoTIFF and ASCII XYZ formats for
    years 2016-2020, with units of people per square kilometer.
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
- href: https://data.humdata.org/dataset/worldpop-population-density-for-ghana
  rel: source
loss: null
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
  description: Ghana - Population Density (The spatial distribution of population
    density in 2020, Ghana)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2020/GHA/gha_pd_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_aeb5e480
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ghana - Population Density (The spatial distribution of population
    density in 2020, Ghana)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2020/GHA/gha_pd_2020_1km.tif
  format: null
  id: resource_66dca115
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2020_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2020 based on country
    total adjusted to match the corresponding UNPD estimate, Ghana
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2020/GHA/gha_pd_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_319be51a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2020 based on country
    total adjusted to match the corresponding UNPD estimate, Ghana
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2020/GHA/gha_pd_2020_1km_UNadj.tif
  format: null
  id: resource_9781e8d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2020_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ghana - Population Density (The spatial distribution of population
    density in 2019, Ghana)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2019/GHA/gha_pd_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_db17ba7a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ghana - Population Density (The spatial distribution of population
    density in 2019, Ghana)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2019/GHA/gha_pd_2019_1km.tif
  format: null
  id: resource_550386b3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2019_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2019 based on country
    total adjusted to match the corresponding UNPD estimate, Ghana
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2019/GHA/gha_pd_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_a50c46d4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2019 based on country
    total adjusted to match the corresponding UNPD estimate, Ghana
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2019/GHA/gha_pd_2019_1km_UNadj.tif
  format: null
  id: resource_b8ca1926
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2019_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ghana - Population Density (The spatial distribution of population
    density in 2018, Ghana)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2018/GHA/gha_pd_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_1e226a79
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ghana - Population Density (The spatial distribution of population
    density in 2018, Ghana)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2018/GHA/gha_pd_2018_1km.tif
  format: null
  id: resource_784ed8f2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2018_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2018 based on country
    total adjusted to match the corresponding UNPD estimate, Ghana
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2018/GHA/gha_pd_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_fb46ea41
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2018 based on country
    total adjusted to match the corresponding UNPD estimate, Ghana
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2018/GHA/gha_pd_2018_1km_UNadj.tif
  format: null
  id: resource_d73e9c68
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2018_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ghana - Population Density (The spatial distribution of population
    density in 2017, Ghana)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2017/GHA/gha_pd_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_7b65efc0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ghana - Population Density (The spatial distribution of population
    density in 2017, Ghana)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2017/GHA/gha_pd_2017_1km.tif
  format: null
  id: resource_613ccbb5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2017_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2017 based on country
    total adjusted to match the corresponding UNPD estimate, Ghana
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2017/GHA/gha_pd_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_86485eef
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2017 based on country
    total adjusted to match the corresponding UNPD estimate, Ghana
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2017/GHA/gha_pd_2017_1km_UNadj.tif
  format: null
  id: resource_7761fe4e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2017_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ghana - Population Density (The spatial distribution of population
    density in 2016, Ghana)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2016/GHA/gha_pd_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_5b889e65
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Ghana - Population Density (The spatial distribution of population
    density in 2016, Ghana)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2016/GHA/gha_pd_2016_1km.tif
  format: null
  id: resource_f103220a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2016_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2016 based on country
    total adjusted to match the corresponding UNPD estimate, Ghana
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2016/GHA/gha_pd_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_4ce9f42e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2016 based on country
    total adjusted to match the corresponding UNPD estimate, Ghana
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2016/GHA/gha_pd_2016_1km_UNadj.tif
  format: null
  id: resource_f0178d88
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gha_pd_2016_1km_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gha_worldpop_populationdensity_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - GHA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Ghana - Population Density
version: null
vulnerability: null
---
