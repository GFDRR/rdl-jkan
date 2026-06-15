---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-somalia
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-somalia
dataset_id: rdls_exp-som_worldpop_populationcounts_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-for-somalia]'
details: null
exposure:
- asset_type:
    description: Gridded population counts at 100m resolution for Somalia, adjusted
      to UN population estimates
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
  description: WorldPop generated gridded population estimates for Somalia using country-specific
    methods applied to 100m resolution raster cells. Population counts per grid cell
    were calibrated to match official UN population estimates for the country. Multiple
    variants are provided including UN-adjusted and constrained versions at different
    spatial resolutions (100m and 1km).
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-for-somalia
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
  url: https://dx.doi.org/10.5258/SOTON/WP00665-
- author_names: null
  date_published: null
  doi: null
  id: reference_3
  name: Methodology documentation
  url: http://digitizeafrica
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2020, Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/SOM/som_ppp_2020.tif
  format: null
  id: resource_b4494e8c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2019, Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/SOM/som_ppp_2019.tif
  format: null
  id: resource_d7e4a4d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2018, Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/SOM/som_ppp_2018.tif
  format: null
  id: resource_0072ab80
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2017, Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/SOM/som_ppp_2017.tif
  format: null
  id: resource_a01c87dc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2016, Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/SOM/som_ppp_2016.tif
  format: null
  id: resource_673dd408
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/SOM/som_ppp_2020_UNadj.tif
  format: null
  id: resource_e3069cbb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2020_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/SOM/som_ppp_2019_UNadj.tif
  format: null
  id: resource_db161475
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2019_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/SOM/som_ppp_2018_UNadj.tif
  format: null
  id: resource_206e5e0b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2018_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/SOM/som_ppp_2017_UNadj.tif
  format: null
  id: resource_b83ca6e7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2017_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/SOM/som_ppp_2016_UNadj.tif
  format: null
  id: resource_e1ca8aea
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2016_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2020, Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/maxar_v1/SOM/som_ppp_2020_constrained.tif
  format: null
  id: resource_8b22191d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2020_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/maxar_v1/SOM/som_ppp_2020_UNadj_constrained.tif
  format: null
  id: resource_4434129a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2020_UNadj_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2020 Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/SOM/som_ppp_2020_1km_Aggregated.tif
  format: null
  id: resource_1caa5308
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2020_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2020 Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/SOM/som_ppp_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_caf6a2a9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/SOM/som_ppp_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_a6e9eef9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/SOM/som_ppp_2020_1km_Aggregated_UNadj.tif
  format: null
  id: resource_c50f7b01
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2020_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2019 Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/SOM/som_ppp_2019_1km_Aggregated.tif
  format: null
  id: resource_856549a5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2019_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2019 Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/SOM/som_ppp_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_ae1e585a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/SOM/som_ppp_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_8d2f5dea
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/SOM/som_ppp_2019_1km_Aggregated_UNadj.tif
  format: null
  id: resource_a41bb182
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2019_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2018 Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/SOM/som_ppp_2018_1km_Aggregated.tif
  format: null
  id: resource_439c5295
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2018_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2018 Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/SOM/som_ppp_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_639445b3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/SOM/som_ppp_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_860a1413
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/SOM/som_ppp_2018_1km_Aggregated_UNadj.tif
  format: null
  id: resource_c9619ff3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2018_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2017 Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/SOM/som_ppp_2017_1km_Aggregated.tif
  format: null
  id: resource_0cda8b4d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2017_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2017 Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/SOM/som_ppp_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_b3d8d022
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/SOM/som_ppp_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_42ce927b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/SOM/som_ppp_2017_1km_Aggregated_UNadj.tif
  format: null
  id: resource_28a7bd64
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2017_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2016 Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/SOM/som_ppp_2016_1km_Aggregated.tif
  format: null
  id: resource_e4b24eff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2016_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Somalia - Population Counts (The spatial distribution of population
    in 2016 Somalia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/SOM/som_ppp_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_09ec9cf7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/SOM/som_ppp_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_4e9bf650
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Somalia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/SOM/som_ppp_2016_1km_Aggregated_UNadj.tif
  format: null
  id: resource_4c39c0ca
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: som_ppp_2016_1km_Aggregated_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-som_worldpop_populationcounts_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - SOM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Somalia - Population Counts
version: null
vulnerability: null
---
