---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-united-kingdom-of-great-britain-and-northern-ireland
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-united-kingdom-of-great-britain-and-northern-ireland
dataset_id: rdls_exp-gbr_worldpop_northernirelandpopulation_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-for-united-kingdom-of-great-britain-and-northern-ireland]'
details: null
exposure:
- asset_type:
    description: Gridded population counts at 100m resolution for the United Kingdom,
      adjusted to official national totals
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
  description: WorldPop gridded population estimates were generated using customized
    spatial modeling methods applied to UK census data and adjusted to match official
    national population totals. The dataset provides 100m resolution population counts
    in GeoTIFF and ASCII XYZ formats for multiple years (2016-2020), with both UN-adjusted
    and unadjusted variants available.
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-for-united-kingdom-of-great-britain-and-northern-ireland
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
  description: The spatial distribution of population in 2020, United Kingdom of Great
    Britain & Northern Ireland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/GBR/gbr_ppp_2020.tif
  format: null
  id: resource_333e9a56
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019, United Kingdom of Great
    Britain & Northern Ireland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/GBR/gbr_ppp_2019.tif
  format: null
  id: resource_b8dac4a9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018, United Kingdom of Great
    Britain & Northern Ireland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/GBR/gbr_ppp_2018.tif
  format: null
  id: resource_7f43c1fe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017, United Kingdom of Great
    Britain & Northern Ireland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/GBR/gbr_ppp_2017.tif
  format: null
  id: resource_04f65020
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016, United Kingdom of Great
    Britain & Northern Ireland
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/GBR/gbr_ppp_2016.tif
  format: null
  id: resource_a8146083
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/GBR/gbr_ppp_2020_UNadj.tif
  format: null
  id: resource_7565f58a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2020_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/GBR/gbr_ppp_2019_UNadj.tif
  format: null
  id: resource_940fd1c9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2019_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/GBR/gbr_ppp_2018_UNadj.tif
  format: null
  id: resource_bf3ec990
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2018_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/GBR/gbr_ppp_2017_UNadj.tif
  format: null
  id: resource_255a7bf2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2017_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/GBR/gbr_ppp_2016_UNadj.tif
  format: null
  id: resource_7b76fb96
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2016_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain and Northern Ireland - Population Counts
    (The spatial distribution of population in 2020, United Kingdom)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/GBR/gbr_ppp_2020_constrained.tif
  format: null
  id: resource_fcd1ee86
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2020_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/GBR/gbr_ppp_2020_UNadj_constrained.tif
  format: null
  id: resource_bc3ee590
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2020_UNadj_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain and Northern Ireland - Population Counts
    (The spatial distribution of population in 2020 United Kingdom)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/GBR/gbr_ppp_2020_1km_Aggregated.tif
  format: null
  id: resource_6d496294
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2020_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain and Northern Ireland - Population Counts
    (The spatial distribution of population in 2020 United Kingdom)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/GBR/gbr_ppp_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_4c7a1b78
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/GBR/gbr_ppp_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_9e11deab
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/GBR/gbr_ppp_2020_1km_Aggregated_UNadj.tif
  format: null
  id: resource_3b3c41d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2020_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain and Northern Ireland - Population Counts
    (The spatial distribution of population in 2019 United Kingdom)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/GBR/gbr_ppp_2019_1km_Aggregated.tif
  format: null
  id: resource_76a42da5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2019_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain and Northern Ireland - Population Counts
    (The spatial distribution of population in 2019 United Kingdom)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/GBR/gbr_ppp_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_b4e67455
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/GBR/gbr_ppp_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_b39bb1c4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/GBR/gbr_ppp_2019_1km_Aggregated_UNadj.tif
  format: null
  id: resource_2e99fe15
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2019_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain and Northern Ireland - Population Counts
    (The spatial distribution of population in 2018 United Kingdom)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/GBR/gbr_ppp_2018_1km_Aggregated.tif
  format: null
  id: resource_c25eded5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2018_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain and Northern Ireland - Population Counts
    (The spatial distribution of population in 2018 United Kingdom)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/GBR/gbr_ppp_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_db843d54
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/GBR/gbr_ppp_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_c6095ec2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/GBR/gbr_ppp_2018_1km_Aggregated_UNadj.tif
  format: null
  id: resource_33aced49
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2018_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain and Northern Ireland - Population Counts
    (The spatial distribution of population in 2017 United Kingdom)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/GBR/gbr_ppp_2017_1km_Aggregated.tif
  format: null
  id: resource_d8d54b63
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2017_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain and Northern Ireland - Population Counts
    (The spatial distribution of population in 2017 United Kingdom)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/GBR/gbr_ppp_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_33a64c49
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/GBR/gbr_ppp_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_a204ce9b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/GBR/gbr_ppp_2017_1km_Aggregated_UNadj.tif
  format: null
  id: resource_a3481c8d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2017_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain and Northern Ireland - Population Counts
    (The spatial distribution of population in 2016 United Kingdom)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/GBR/gbr_ppp_2016_1km_Aggregated.tif
  format: null
  id: resource_e3d527b5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2016_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain and Northern Ireland - Population Counts
    (The spatial distribution of population in 2016 United Kingdom)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/GBR/gbr_ppp_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_fe2eabc4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/GBR/gbr_ppp_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_e69c2927
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, United Kingdom
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/GBR/gbr_ppp_2016_1km_Aggregated_UNadj.tif
  format: null
  id: resource_923928c4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_ppp_2016_1km_Aggregated_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gbr_worldpop_northernirelandpopulation_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - GBR
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: United Kingdom of Great Britain and Northern Ireland - Population Counts
version: null
vulnerability: null
---
