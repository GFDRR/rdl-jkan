---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-austria
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-austria
dataset_id: rdls_exp-aut_worldpop_populationcounts_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-for-austria]'
details: null
exposure:
- asset_type:
    description: Gridded population counts at 100m resolution for Austria, adjusted
      to official national totals
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
  description: WorldPop produced gridded population estimates for Austria using customized
    methods applied to census and ancillary geospatial data, generating 100m resolution
    rasters adjusted to match official national population totals, with multiple variants
    (UN-adjusted, constrained, aggregated to 1km) provided across multiple years (2016-2020).
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-for-austria
  rel: source
loss: null
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
  description: Austria - Population Counts (The spatial distribution of population
    in 2020, Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/AUT/aut_ppp_2020.tif
  format: null
  id: resource_983094fc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2019, Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/AUT/aut_ppp_2019.tif
  format: null
  id: resource_65420083
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2018, Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/AUT/aut_ppp_2018.tif
  format: null
  id: resource_c96a6236
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2017, Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/AUT/aut_ppp_2017.tif
  format: null
  id: resource_90384a52
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2016, Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/AUT/aut_ppp_2016.tif
  format: null
  id: resource_323fc7f7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/AUT/aut_ppp_2020_UNadj.tif
  format: null
  id: resource_14289578
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2020_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/AUT/aut_ppp_2019_UNadj.tif
  format: null
  id: resource_847f456c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2019_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/AUT/aut_ppp_2018_UNadj.tif
  format: null
  id: resource_c47cbf5c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2018_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/AUT/aut_ppp_2017_UNadj.tif
  format: null
  id: resource_72c2b774
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2017_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/AUT/aut_ppp_2016_UNadj.tif
  format: null
  id: resource_8c8d7751
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2016_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2020, Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/AUT/aut_ppp_2020_constrained.tif
  format: null
  id: resource_766c7d8a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2020_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/AUT/aut_ppp_2020_UNadj_constrained.tif
  format: null
  id: resource_ec7df9a2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2020_UNadj_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2020 Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/AUT/aut_ppp_2020_1km_Aggregated.tif
  format: null
  id: resource_77d2aad7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2020_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2020 Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/AUT/aut_ppp_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_41ecd220
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/AUT/aut_ppp_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_834c4422
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/AUT/aut_ppp_2020_1km_Aggregated_UNadj.tif
  format: null
  id: resource_6468edbd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2020_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2019 Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/AUT/aut_ppp_2019_1km_Aggregated.tif
  format: null
  id: resource_97b3debb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2019_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2019 Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/AUT/aut_ppp_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_312d483a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/AUT/aut_ppp_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_73dba074
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/AUT/aut_ppp_2019_1km_Aggregated_UNadj.tif
  format: null
  id: resource_d4759ead
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2019_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2018 Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/AUT/aut_ppp_2018_1km_Aggregated.tif
  format: null
  id: resource_d729b8c0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2018_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2018 Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/AUT/aut_ppp_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_f1e54c37
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/AUT/aut_ppp_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_a8414fe7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/AUT/aut_ppp_2018_1km_Aggregated_UNadj.tif
  format: null
  id: resource_8eee1d19
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2018_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2017 Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/AUT/aut_ppp_2017_1km_Aggregated.tif
  format: null
  id: resource_5d64dfa6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2017_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2017 Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/AUT/aut_ppp_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_27b2eb6d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/AUT/aut_ppp_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_66d7791c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/AUT/aut_ppp_2017_1km_Aggregated_UNadj.tif
  format: null
  id: resource_360562a3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2017_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2016 Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/AUT/aut_ppp_2016_1km_Aggregated.tif
  format: null
  id: resource_bb808ca6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2016_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Austria - Population Counts (The spatial distribution of population
    in 2016 Austria)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/AUT/aut_ppp_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_9669ea89
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/AUT/aut_ppp_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_b8d04395
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Austria
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/AUT/aut_ppp_2016_1km_Aggregated_UNadj.tif
  format: null
  id: resource_2cdc1ca5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: aut_ppp_2016_1km_Aggregated_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-aut_worldpop_populationcounts_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - AUT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Austria - Population Counts
version: null
vulnerability: null
---
