---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop, University of Southampton, UK
    url: https://data.humdata.org/dataset/worldpop-population-density-for-romania
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-density-for-romania
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-density-for-romania
dataset_id: rdls_exp-rou_worldpop_populationdensity_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-density-for-romania]'
details: null
exposure:
- asset_type:
    description: "Gridded population density for Romania at 1km resolution (persons\
      \ per km\xB2) for years 2016\u20132020, with and without UN adjustment"
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
  description: "Census-derived population counts for Romania are spatially disaggregated\
    \ to a 30 arc-second (~1km) grid using WorldPop's dasymetric modelling approach,\
    \ incorporating ancillary geospatial covariates. UN-adjusted variants rescale\
    \ the modelled totals to match UN national population estimates. Annual layers\
    \ are produced for 2016\u20132020 and distributed in GeoTIFF and ASCII XYZ formats\
    \ under WGS84 projection."
  sources:
  - id: source_1
    license: null
    name: WorldPop, University of Southampton, UK
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/worldpop-population-density-for-romania
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
  description: Romania - Population Density (The spatial distribution of population
    density in 2020, Romania)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2020/ROU/rou_pd_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_8d3a1f1b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Romania - Population Density (The spatial distribution of population
    density in 2020, Romania)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2020/ROU/rou_pd_2020_1km.tif
  format: null
  id: resource_0378f2ee
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2020_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2020 based on country
    total adjusted to match the corresponding UNPD estimate, Romania
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2020/ROU/rou_pd_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_d7ec1e11
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2020 based on country
    total adjusted to match the corresponding UNPD estimate, Romania
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2020/ROU/rou_pd_2020_1km_UNadj.tif
  format: null
  id: resource_4e9c3660
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2020_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Romania - Population Density (The spatial distribution of population
    density in 2019, Romania)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2019/ROU/rou_pd_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_54ad930d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Romania - Population Density (The spatial distribution of population
    density in 2019, Romania)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2019/ROU/rou_pd_2019_1km.tif
  format: null
  id: resource_a44453bf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2019_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2019 based on country
    total adjusted to match the corresponding UNPD estimate, Romania
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2019/ROU/rou_pd_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_1a710a09
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2019 based on country
    total adjusted to match the corresponding UNPD estimate, Romania
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2019/ROU/rou_pd_2019_1km_UNadj.tif
  format: null
  id: resource_14d108b2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2019_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Romania - Population Density (The spatial distribution of population
    density in 2018, Romania)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2018/ROU/rou_pd_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_28d1616f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Romania - Population Density (The spatial distribution of population
    density in 2018, Romania)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2018/ROU/rou_pd_2018_1km.tif
  format: null
  id: resource_50098d1c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2018_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2018 based on country
    total adjusted to match the corresponding UNPD estimate, Romania
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2018/ROU/rou_pd_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_c8a12e73
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2018 based on country
    total adjusted to match the corresponding UNPD estimate, Romania
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2018/ROU/rou_pd_2018_1km_UNadj.tif
  format: null
  id: resource_2752baa3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2018_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Romania - Population Density (The spatial distribution of population
    density in 2017, Romania)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2017/ROU/rou_pd_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_7c4b36ec
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Romania - Population Density (The spatial distribution of population
    density in 2017, Romania)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2017/ROU/rou_pd_2017_1km.tif
  format: null
  id: resource_88f09120
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2017_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2017 based on country
    total adjusted to match the corresponding UNPD estimate, Romania
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2017/ROU/rou_pd_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_6180a96b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2017 based on country
    total adjusted to match the corresponding UNPD estimate, Romania
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2017/ROU/rou_pd_2017_1km_UNadj.tif
  format: null
  id: resource_0a12cfd8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2017_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Romania - Population Density (The spatial distribution of population
    density in 2016, Romania)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2016/ROU/rou_pd_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_158870bf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Romania - Population Density (The spatial distribution of population
    density in 2016, Romania)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2016/ROU/rou_pd_2016_1km.tif
  format: null
  id: resource_91b80bec
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2016_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2016 based on country
    total adjusted to match the corresponding UNPD estimate, Romania
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2016/ROU/rou_pd_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_1719af76
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2016 based on country
    total adjusted to match the corresponding UNPD estimate, Romania
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2016/ROU/rou_pd_2016_1km_UNadj.tif
  format: null
  id: resource_da274785
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rou_pd_2016_1km_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-rou_worldpop_populationdensity_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - ROU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Romania - Population Density
version: null
vulnerability: null
---
