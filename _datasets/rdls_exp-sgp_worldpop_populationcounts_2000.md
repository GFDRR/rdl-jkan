---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop, University of Southampton, UK
    url: https://data.humdata.org/dataset/worldpop-population-counts-for-singapore
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-singapore
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-singapore
dataset_id: rdls_exp-sgp_worldpop_populationcounts_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-for-singapore]'
details: null
exposure:
- asset_type:
    description: Gridded population counts at 100m resolution for Singapore, adjusted
      to official UN estimates
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
  description: WorldPop produced gridded population estimates for Singapore using
    bespoke country-specific methods applied to census and ancillary geospatial data.
    The resulting 100m resolution raster datasets were adjusted to match official
    UN population totals and are provided in multiple formats (GeoTIFF, ASCII XYZ)
    across multiple years (2016-2020) with both adjusted and unadjusted variants.
  sources:
  - id: source_1
    license: null
    name: WorldPop, University of Southampton, UK
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/worldpop-population-counts-for-singapore
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
  description: Singapore - Population Counts (The spatial distribution of population
    in 2020, Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/SGP/sgp_ppp_2020.tif
  format: null
  id: resource_ff0837f7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2019, Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/SGP/sgp_ppp_2019.tif
  format: null
  id: resource_99863f68
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2018, Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/SGP/sgp_ppp_2018.tif
  format: null
  id: resource_3ba3be50
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2017, Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/SGP/sgp_ppp_2017.tif
  format: null
  id: resource_2575fc92
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2016, Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/SGP/sgp_ppp_2016.tif
  format: null
  id: resource_877704d0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/SGP/sgp_ppp_2020_UNadj.tif
  format: null
  id: resource_2e74345b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2020_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/SGP/sgp_ppp_2019_UNadj.tif
  format: null
  id: resource_fee56745
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2019_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/SGP/sgp_ppp_2018_UNadj.tif
  format: null
  id: resource_b921eb32
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2018_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/SGP/sgp_ppp_2017_UNadj.tif
  format: null
  id: resource_f2327a93
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2017_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/SGP/sgp_ppp_2016_UNadj.tif
  format: null
  id: resource_17d17ed6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2016_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2020, Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/SGP/sgp_ppp_2020_constrained.tif
  format: null
  id: resource_5deff53d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2020_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/SGP/sgp_ppp_2020_UNadj_constrained.tif
  format: null
  id: resource_63e2235d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2020_UNadj_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2020 Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/SGP/sgp_ppp_2020_1km_Aggregated.tif
  format: null
  id: resource_44b1128c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2020_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2020 Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/SGP/sgp_ppp_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_80a6fb3c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/SGP/sgp_ppp_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_f3593a8d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/SGP/sgp_ppp_2020_1km_Aggregated_UNadj.tif
  format: null
  id: resource_07ff851c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2020_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2019 Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/SGP/sgp_ppp_2019_1km_Aggregated.tif
  format: null
  id: resource_8a666f51
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2019_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2019 Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/SGP/sgp_ppp_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_c55247ba
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/SGP/sgp_ppp_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_246647b6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/SGP/sgp_ppp_2019_1km_Aggregated_UNadj.tif
  format: null
  id: resource_adb073e8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2019_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2018 Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/SGP/sgp_ppp_2018_1km_Aggregated.tif
  format: null
  id: resource_b0783243
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2018_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2018 Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/SGP/sgp_ppp_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_cacb0de1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/SGP/sgp_ppp_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_5bafe336
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/SGP/sgp_ppp_2018_1km_Aggregated_UNadj.tif
  format: null
  id: resource_ec26e563
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2018_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2017 Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/SGP/sgp_ppp_2017_1km_Aggregated.tif
  format: null
  id: resource_c39761c7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2017_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2017 Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/SGP/sgp_ppp_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_03a54dbf
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/SGP/sgp_ppp_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_97504f45
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/SGP/sgp_ppp_2017_1km_Aggregated_UNadj.tif
  format: null
  id: resource_6b2e14cb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2017_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2016 Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/SGP/sgp_ppp_2016_1km_Aggregated.tif
  format: null
  id: resource_c576d1d8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2016_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Singapore - Population Counts (The spatial distribution of population
    in 2016 Singapore)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/SGP/sgp_ppp_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_a914e313
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/SGP/sgp_ppp_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_3052eba1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Singapore
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/SGP/sgp_ppp_2016_1km_Aggregated_UNadj.tif
  format: null
  id: resource_4dbd0051
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: sgp_ppp_2016_1km_Aggregated_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-sgp_worldpop_populationcounts_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - SGP
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Singapore - Population Counts
version: null
vulnerability: null
---
