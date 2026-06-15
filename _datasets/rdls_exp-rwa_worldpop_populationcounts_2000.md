---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop, University of Southampton
    url: https://data.humdata.org/dataset/worldpop-population-counts-for-rwanda
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-rwanda
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-rwanda
dataset_id: rdls_exp-rwa_worldpop_populationcounts_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-for-rwanda]'
details: null
exposure:
- asset_type:
    description: Gridded population counts at 100m resolution, adjusted to UN population
      estimates
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
  description: WorldPop produced gridded population estimates at 100m resolution using
    country-specific customized methods. Population counts per grid cell were adjusted
    to match official United Nations population estimates. Multiple variants are provided
    including UN-adjusted and constrained versions at different spatial resolutions
    (100m and 1km).
  sources:
  - id: source_1
    license: null
    name: WorldPop, University of Southampton
    risk_data_type:
    - exposure
    type: dataset
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/worldpop-population-counts-for-rwanda
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
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2020, Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/RWA/rwa_ppp_2020.tif
  format: null
  id: resource_266f3a85
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2019, Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/RWA/rwa_ppp_2019.tif
  format: null
  id: resource_488ae755
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2018, Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/RWA/rwa_ppp_2018.tif
  format: null
  id: resource_e816d86f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2017, Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/RWA/rwa_ppp_2017.tif
  format: null
  id: resource_d72e2c58
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2016, Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/RWA/rwa_ppp_2016.tif
  format: null
  id: resource_3189ceee
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/RWA/rwa_ppp_2020_UNadj.tif
  format: null
  id: resource_d8e713ec
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2020_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/RWA/rwa_ppp_2019_UNadj.tif
  format: null
  id: resource_01388ceb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2019_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/RWA/rwa_ppp_2018_UNadj.tif
  format: null
  id: resource_d0509ad4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2018_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/RWA/rwa_ppp_2017_UNadj.tif
  format: null
  id: resource_b75618a2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2017_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/RWA/rwa_ppp_2016_UNadj.tif
  format: null
  id: resource_129c57e7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2016_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2020, Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/maxar_v1/RWA/rwa_ppp_2020_constrained.tif
  format: null
  id: resource_ccee487c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2020_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/maxar_v1/RWA/rwa_ppp_2020_UNadj_constrained.tif
  format: null
  id: resource_de4ba6c0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2020_UNadj_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2020 Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/RWA/rwa_ppp_2020_1km_Aggregated.tif
  format: null
  id: resource_adbf97e6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2020_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2020 Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/RWA/rwa_ppp_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_0ec1d836
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/RWA/rwa_ppp_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_0f61d1f2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/RWA/rwa_ppp_2020_1km_Aggregated_UNadj.tif
  format: null
  id: resource_31f28b64
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2020_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2019 Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/RWA/rwa_ppp_2019_1km_Aggregated.tif
  format: null
  id: resource_f4208fc9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2019_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2019 Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/RWA/rwa_ppp_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_f70f0724
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/RWA/rwa_ppp_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_798bd0ef
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/RWA/rwa_ppp_2019_1km_Aggregated_UNadj.tif
  format: null
  id: resource_446a1452
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2019_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2018 Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/RWA/rwa_ppp_2018_1km_Aggregated.tif
  format: null
  id: resource_5a0b1633
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2018_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2018 Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/RWA/rwa_ppp_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_2ae91861
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/RWA/rwa_ppp_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_a242e54b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/RWA/rwa_ppp_2018_1km_Aggregated_UNadj.tif
  format: null
  id: resource_e65c6c3e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2018_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2017 Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/RWA/rwa_ppp_2017_1km_Aggregated.tif
  format: null
  id: resource_1b28f20f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2017_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2017 Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/RWA/rwa_ppp_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_4b818d70
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/RWA/rwa_ppp_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_a0fdf944
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/RWA/rwa_ppp_2017_1km_Aggregated_UNadj.tif
  format: null
  id: resource_82113bd4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2017_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2016 Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/RWA/rwa_ppp_2016_1km_Aggregated.tif
  format: null
  id: resource_64858630
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2016_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Rwanda - Population Counts (The spatial distribution of population
    in 2016 Rwanda)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/RWA/rwa_ppp_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_e0342b47
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/RWA/rwa_ppp_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_f118ed5d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Rwanda
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/RWA/rwa_ppp_2016_1km_Aggregated_UNadj.tif
  format: null
  id: resource_1a1be510
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: rwa_ppp_2016_1km_Aggregated_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-rwa_worldpop_populationcounts_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - RWA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Rwanda - Population Counts
version: null
vulnerability: null
---
