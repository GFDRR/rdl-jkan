---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-kingdom-of-eswatini
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-kingdom-of-eswatini
dataset_id: rdls_exp-swz_worldpop_kingdompopulationcounts_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-for-kingdom-of-eswatini]'
details: null
exposure:
- asset_type:
    description: Gridded population counts at 100m resolution for Kingdom of Eswatini,
      adjusted to UN population estimates
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
  description: WorldPop produced gridded population estimates for Eswatini at 100m
    resolution using country-specific customized methods. Population counts per grid
    cell were derived from census and survey data and adjusted to match official UN
    population estimates. Multiple variants are provided including UN-adjusted and
    constrained versions at different spatial resolutions (100m and 1km).
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-for-kingdom-of-eswatini
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
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2020, Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/SWZ/swz_ppp_2020.tif
  format: null
  id: resource_831169a1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2019, Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/SWZ/swz_ppp_2019.tif
  format: null
  id: resource_aa017ed1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2018, Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/SWZ/swz_ppp_2018.tif
  format: null
  id: resource_c0fd1151
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2017, Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/SWZ/swz_ppp_2017.tif
  format: null
  id: resource_f83e138e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2016, Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/SWZ/swz_ppp_2016.tif
  format: null
  id: resource_12b57dfc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/SWZ/swz_ppp_2020_UNadj.tif
  format: null
  id: resource_a7471fa4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2020_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/SWZ/swz_ppp_2019_UNadj.tif
  format: null
  id: resource_8fb05c58
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2019_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/SWZ/swz_ppp_2018_UNadj.tif
  format: null
  id: resource_aa4b75d8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2018_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/SWZ/swz_ppp_2017_UNadj.tif
  format: null
  id: resource_1674489c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2017_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/SWZ/swz_ppp_2016_UNadj.tif
  format: null
  id: resource_b9a4a49c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2016_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2020, Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/maxar_v1/SWZ/swz_ppp_2020_constrained.tif
  format: null
  id: resource_a8f9ef50
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2020_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/maxar_v1/SWZ/swz_ppp_2020_UNadj_constrained.tif
  format: null
  id: resource_6fc91ab9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2020_UNadj_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2020 Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/SWZ/swz_ppp_2020_1km_Aggregated.tif
  format: null
  id: resource_a8432f85
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2020_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2020 Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/SWZ/swz_ppp_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_6d9b457f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/SWZ/swz_ppp_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_12a7e361
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/SWZ/swz_ppp_2020_1km_Aggregated_UNadj.tif
  format: null
  id: resource_3cd2dc07
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2020_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2019 Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/SWZ/swz_ppp_2019_1km_Aggregated.tif
  format: null
  id: resource_96078560
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2019_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2019 Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/SWZ/swz_ppp_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_3e63e5e5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/SWZ/swz_ppp_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_aa00ef2e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/SWZ/swz_ppp_2019_1km_Aggregated_UNadj.tif
  format: null
  id: resource_8d2dd594
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2019_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2018 Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/SWZ/swz_ppp_2018_1km_Aggregated.tif
  format: null
  id: resource_202221b2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2018_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2018 Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/SWZ/swz_ppp_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_ea2e8eea
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/SWZ/swz_ppp_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_50c419c9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/SWZ/swz_ppp_2018_1km_Aggregated_UNadj.tif
  format: null
  id: resource_f46b2e8c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2018_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2017 Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/SWZ/swz_ppp_2017_1km_Aggregated.tif
  format: null
  id: resource_903f4537
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2017_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2017 Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/SWZ/swz_ppp_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_5e4ed54c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/SWZ/swz_ppp_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_50d3fa0f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/SWZ/swz_ppp_2017_1km_Aggregated_UNadj.tif
  format: null
  id: resource_143c8a97
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2017_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2016 Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/SWZ/swz_ppp_2016_1km_Aggregated.tif
  format: null
  id: resource_54b2b018
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2016_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kingdom of Eswatini - Population Counts (The spatial distribution of
    population in 2016 Swaziland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/SWZ/swz_ppp_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_d6a6d684
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/SWZ/swz_ppp_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_23382b26
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Swaziland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/SWZ/swz_ppp_2016_1km_Aggregated_UNadj.tif
  format: null
  id: resource_4c78c4b2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: swz_ppp_2016_1km_Aggregated_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-swz_worldpop_kingdompopulationcounts_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - SWZ
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Kingdom of Eswatini - Population Counts
version: null
vulnerability: null
---
