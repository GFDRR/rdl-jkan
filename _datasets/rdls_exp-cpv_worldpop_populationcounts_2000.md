---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-cabo-verde
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-cabo-verde
dataset_id: rdls_exp-cpv_worldpop_populationcounts_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-for-cabo-verde]'
details: null
exposure:
- asset_type:
    description: Gridded population counts at 100m resolution for Cabo Verde, adjusted
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
license: CC-BY-4.0
lineage:
  description: WorldPop produced gridded population estimates at 100m resolution using
    country-specific customized methods. Population counts per grid cell were derived
    from census and survey data and adjusted to match official UN population estimates
    for Cabo Verde, with multiple variants provided (UN-adjusted, unadjusted, and
    constrained versions) across multiple years (2016-2020).
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-for-cabo-verde
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
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2020, Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/CPV/cpv_ppp_2020.tif
  format: null
  id: resource_54fd1208
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2019, Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/CPV/cpv_ppp_2019.tif
  format: null
  id: resource_a39c5f25
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2018, Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/CPV/cpv_ppp_2018.tif
  format: null
  id: resource_9babdd4e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2017, Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/CPV/cpv_ppp_2017.tif
  format: null
  id: resource_ef5f1304
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2016, Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/CPV/cpv_ppp_2016.tif
  format: null
  id: resource_e2de1773
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/CPV/cpv_ppp_2020_UNadj.tif
  format: null
  id: resource_842a6275
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2020_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/CPV/cpv_ppp_2019_UNadj.tif
  format: null
  id: resource_2536ba09
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2019_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/CPV/cpv_ppp_2018_UNadj.tif
  format: null
  id: resource_3f23ad6e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2018_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/CPV/cpv_ppp_2017_UNadj.tif
  format: null
  id: resource_20d70c3e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2017_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/CPV/cpv_ppp_2016_UNadj.tif
  format: null
  id: resource_732f7a16
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2016_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2020, Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/maxar_v1/CPV/cpv_ppp_2020_constrained.tif
  format: null
  id: resource_ba9d1304
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2020_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/maxar_v1/CPV/cpv_ppp_2020_UNadj_constrained.tif
  format: null
  id: resource_c6149d85
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2020_UNadj_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2020 Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/CPV/cpv_ppp_2020_1km_Aggregated.tif
  format: null
  id: resource_394bca0b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2020_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2020 Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/CPV/cpv_ppp_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_4bb71086
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/CPV/cpv_ppp_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_90a3df05
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/CPV/cpv_ppp_2020_1km_Aggregated_UNadj.tif
  format: null
  id: resource_e25d6766
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2020_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2019 Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/CPV/cpv_ppp_2019_1km_Aggregated.tif
  format: null
  id: resource_7d14c485
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2019_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2019 Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/CPV/cpv_ppp_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_e5899252
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/CPV/cpv_ppp_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_dabd5e8d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/CPV/cpv_ppp_2019_1km_Aggregated_UNadj.tif
  format: null
  id: resource_2f736348
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2019_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2018 Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/CPV/cpv_ppp_2018_1km_Aggregated.tif
  format: null
  id: resource_6100ae58
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2018_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2018 Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/CPV/cpv_ppp_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_e791f545
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/CPV/cpv_ppp_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_6d973fa0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/CPV/cpv_ppp_2018_1km_Aggregated_UNadj.tif
  format: null
  id: resource_6a8a1391
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2018_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2017 Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/CPV/cpv_ppp_2017_1km_Aggregated.tif
  format: null
  id: resource_74c0582a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2017_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2017 Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/CPV/cpv_ppp_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_af5c37c7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/CPV/cpv_ppp_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_8e62118a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/CPV/cpv_ppp_2017_1km_Aggregated_UNadj.tif
  format: null
  id: resource_2270d3f5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2017_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2016 Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/CPV/cpv_ppp_2016_1km_Aggregated.tif
  format: null
  id: resource_e422a083
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2016_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Cabo Verde - Population Counts (The spatial distribution of population
    in 2016 Cape Verde)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/CPV/cpv_ppp_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_4a2ce48a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/CPV/cpv_ppp_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_0dc4918d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Cape Verde
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/CPV/cpv_ppp_2016_1km_Aggregated_UNadj.tif
  format: null
  id: resource_15593a35
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cpv_ppp_2016_1km_Aggregated_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-cpv_worldpop_populationcounts_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - CPV
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Cabo Verde - Population Counts
version: null
vulnerability: null
---
