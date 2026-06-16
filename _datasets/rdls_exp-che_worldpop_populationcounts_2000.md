---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-switzerland
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-switzerland
dataset_id: rdls_exp-che_worldpop_populationcounts_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-for-switzerland]'
details: null
exposure:
- asset_type:
    description: Gridded population counts at 100m resolution for Switzerland, adjusted
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
  description: WorldPop gridded population estimates for Switzerland were generated
    using customized spatial modeling methods applied to census data and adjusted
    to match official national population totals. The dataset provides 100m resolution
    population counts in multiple formats (GeoTIFF and ASCII XYZ) for multiple years
    (2016-2020), with both UN-adjusted and unadjusted variants available.
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-for-switzerland
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
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2020, Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/CHE/che_ppp_2020.tif
  format: null
  id: resource_5acb3dae
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2019, Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/CHE/che_ppp_2019.tif
  format: null
  id: resource_49f3b046
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2018, Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/CHE/che_ppp_2018.tif
  format: null
  id: resource_e0fe1930
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2017, Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/CHE/che_ppp_2017.tif
  format: null
  id: resource_bb827923
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2016, Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/CHE/che_ppp_2016.tif
  format: null
  id: resource_5dfb84b5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/CHE/che_ppp_2020_UNadj.tif
  format: null
  id: resource_d4e38f86
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2020_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/CHE/che_ppp_2019_UNadj.tif
  format: null
  id: resource_073081dd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2019_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/CHE/che_ppp_2018_UNadj.tif
  format: null
  id: resource_aae9ad0a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2018_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/CHE/che_ppp_2017_UNadj.tif
  format: null
  id: resource_efa485e3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2017_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/CHE/che_ppp_2016_UNadj.tif
  format: null
  id: resource_c90e32ea
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2016_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2020, Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/CHE/che_ppp_2020_constrained.tif
  format: null
  id: resource_cfb47902
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2020_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/CHE/che_ppp_2020_UNadj_constrained.tif
  format: null
  id: resource_1acc9a08
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2020_UNadj_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2020 Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/CHE/che_ppp_2020_1km_Aggregated.tif
  format: null
  id: resource_83e6cf0b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2020_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2020 Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/CHE/che_ppp_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_1ebc23a5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/CHE/che_ppp_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_0b18183f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/CHE/che_ppp_2020_1km_Aggregated_UNadj.tif
  format: null
  id: resource_99b47906
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2020_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2019 Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/CHE/che_ppp_2019_1km_Aggregated.tif
  format: null
  id: resource_852f88c2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2019_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2019 Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/CHE/che_ppp_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_6760f089
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/CHE/che_ppp_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_a220f7f9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/CHE/che_ppp_2019_1km_Aggregated_UNadj.tif
  format: null
  id: resource_b9ce8bad
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2019_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2018 Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/CHE/che_ppp_2018_1km_Aggregated.tif
  format: null
  id: resource_1760c8d4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2018_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2018 Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/CHE/che_ppp_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_855a3fcb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/CHE/che_ppp_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_c66cb158
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/CHE/che_ppp_2018_1km_Aggregated_UNadj.tif
  format: null
  id: resource_80e8db56
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2018_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2017 Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/CHE/che_ppp_2017_1km_Aggregated.tif
  format: null
  id: resource_62de1668
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2017_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2017 Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/CHE/che_ppp_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_44fa55bc
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/CHE/che_ppp_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_8a8049c1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/CHE/che_ppp_2017_1km_Aggregated_UNadj.tif
  format: null
  id: resource_90bca423
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2017_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2016 Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/CHE/che_ppp_2016_1km_Aggregated.tif
  format: null
  id: resource_8de3f994
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2016_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Switzerland - Population Counts (The spatial distribution of population
    in 2016 Switzerland)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/CHE/che_ppp_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_cc3b2195
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/CHE/che_ppp_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_3f60a67c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Switzerland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/CHE/che_ppp_2016_1km_Aggregated_UNadj.tif
  format: null
  id: resource_641a4b0a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: che_ppp_2016_1km_Aggregated_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-che_worldpop_populationcounts_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - CHE
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Switzerland - Population Counts
version: null
vulnerability: null
---
