---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop, University of Southampton, UK
    url: https://data.humdata.org/dataset/worldpop-population-density-for-malta
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-density-for-malta
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-density-for-malta
dataset_id: rdls_exp-mlt_worldpop_maltapopulationdensity_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-density-for-malta]'
details: null
exposure:
- asset_type:
    description: Gridded population density for Malta at 1km resolution, available
      annually from 2016 to 2020, with and without UN adjustment
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
  description: "Census-derived population counts are disaggregated to a 30 arc-second\
    \ (~1km) grid using WorldPop's dasymetric modelling approach, incorporating ancillary\
    \ geospatial covariates. Two variants are produced: unconstrained estimates and\
    \ UN-adjusted estimates that are normalised to match UN national population totals.\
    \ Annual layers are generated for 2016\xE2\u20AC\u201C2020 for Malta."
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
- href: https://data.humdata.org/dataset/worldpop-population-density-for-malta
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
  description: Malta - Population Density (The spatial distribution of population
    density in 2020, Malta)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2020/MLT/mlt_pd_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_8e30d661
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malta - Population Density (The spatial distribution of population
    density in 2020, Malta)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2020/MLT/mlt_pd_2020_1km.tif
  format: null
  id: resource_9efbbf7b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2020_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2020 based on country
    total adjusted to match the corresponding UNPD estimate, Malta
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2020/MLT/mlt_pd_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_5c51a5e7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2020 based on country
    total adjusted to match the corresponding UNPD estimate, Malta
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2020/MLT/mlt_pd_2020_1km_UNadj.tif
  format: null
  id: resource_488204ce
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2020_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malta - Population Density (The spatial distribution of population
    density in 2019, Malta)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2019/MLT/mlt_pd_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_22bddd97
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malta - Population Density (The spatial distribution of population
    density in 2019, Malta)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2019/MLT/mlt_pd_2019_1km.tif
  format: null
  id: resource_fbc0abd7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2019_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2019 based on country
    total adjusted to match the corresponding UNPD estimate, Malta
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2019/MLT/mlt_pd_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_c984fa37
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2019 based on country
    total adjusted to match the corresponding UNPD estimate, Malta
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2019/MLT/mlt_pd_2019_1km_UNadj.tif
  format: null
  id: resource_1b829420
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2019_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malta - Population Density (The spatial distribution of population
    density in 2018, Malta)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2018/MLT/mlt_pd_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_7deb949f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malta - Population Density (The spatial distribution of population
    density in 2018, Malta)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2018/MLT/mlt_pd_2018_1km.tif
  format: null
  id: resource_1a536a9d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2018_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2018 based on country
    total adjusted to match the corresponding UNPD estimate, Malta
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2018/MLT/mlt_pd_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_082ddfc0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2018 based on country
    total adjusted to match the corresponding UNPD estimate, Malta
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2018/MLT/mlt_pd_2018_1km_UNadj.tif
  format: null
  id: resource_25b1421d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2018_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malta - Population Density (The spatial distribution of population
    density in 2017, Malta)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2017/MLT/mlt_pd_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_f386fb01
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malta - Population Density (The spatial distribution of population
    density in 2017, Malta)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2017/MLT/mlt_pd_2017_1km.tif
  format: null
  id: resource_c1987a95
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2017_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2017 based on country
    total adjusted to match the corresponding UNPD estimate, Malta
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2017/MLT/mlt_pd_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_a1ce8b05
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2017 based on country
    total adjusted to match the corresponding UNPD estimate, Malta
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2017/MLT/mlt_pd_2017_1km_UNadj.tif
  format: null
  id: resource_4470d979
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2017_1km_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malta - Population Density (The spatial distribution of population
    density in 2016, Malta)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2016/MLT/mlt_pd_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_2923f75f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malta - Population Density (The spatial distribution of population
    density in 2016, Malta)
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km/2016/MLT/mlt_pd_2016_1km.tif
  format: null
  id: resource_86ddbac4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2016_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2016 based on country
    total adjusted to match the corresponding UNPD estimate, Malta
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2016/MLT/mlt_pd_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_16f4a2e6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population density in 2016 based on country
    total adjusted to match the corresponding UNPD estimate, Malta
  download_url: https://data.worldpop.org/GIS/Population_Density/Global_2000_2020_1km_UNadj/2016/MLT/mlt_pd_2016_1km_UNadj.tif
  format: null
  id: resource_d9fe9c05
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mlt_pd_2016_1km_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mlt_worldpop_maltapopulationdensity_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - MLT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Malta - Population Density
version: null
vulnerability: null
---
