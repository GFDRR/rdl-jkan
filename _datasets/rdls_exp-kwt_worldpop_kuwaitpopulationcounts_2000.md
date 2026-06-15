---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop, University of Southampton, UK
    url: https://data.humdata.org/dataset/worldpop-population-counts-for-kuwait
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-kuwait
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-kuwait
dataset_id: rdls_exp-kwt_worldpop_kuwaitpopulationcounts_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-for-kuwait]'
details: null
exposure:
- asset_type:
    description: Gridded population counts at 100m resolution for Kuwait, adjusted
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
  description: WorldPop produced gridded population estimates for Kuwait using bespoke
    country-specific methods applied to census and ancillary data. The resulting 100m
    resolution raster datasets were aggregated to 1km resolution and adjusted to match
    official UN population totals, with multiple variants provided (constrained, unadjusted,
    and aggregated formats) across multiple years (2016-2020).
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-for-kuwait
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
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2020, Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/KWT/kwt_ppp_2020.tif
  format: null
  id: resource_8cbc4158
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2019, Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/KWT/kwt_ppp_2019.tif
  format: null
  id: resource_37313025
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2018, Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/KWT/kwt_ppp_2018.tif
  format: null
  id: resource_7a774033
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2017, Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/KWT/kwt_ppp_2017.tif
  format: null
  id: resource_14a24181
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2016, Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/KWT/kwt_ppp_2016.tif
  format: null
  id: resource_a128317e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/KWT/kwt_ppp_2020_UNadj.tif
  format: null
  id: resource_ddaa0b4f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2020_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/KWT/kwt_ppp_2019_UNadj.tif
  format: null
  id: resource_3b6d4335
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2019_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/KWT/kwt_ppp_2018_UNadj.tif
  format: null
  id: resource_9fddfc3d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2018_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/KWT/kwt_ppp_2017_UNadj.tif
  format: null
  id: resource_c7a03649
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2017_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/KWT/kwt_ppp_2016_UNadj.tif
  format: null
  id: resource_d5248cc3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2016_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2020, Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/KWT/kwt_ppp_2020_constrained.tif
  format: null
  id: resource_13da797b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2020_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/KWT/kwt_ppp_2020_UNadj_constrained.tif
  format: null
  id: resource_ed5e6ed3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2020_UNadj_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2020 Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/KWT/kwt_ppp_2020_1km_Aggregated.tif
  format: null
  id: resource_6ae85c6c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2020_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2020 Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/KWT/kwt_ppp_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_10ac154b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/KWT/kwt_ppp_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_fa3d1c3f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/KWT/kwt_ppp_2020_1km_Aggregated_UNadj.tif
  format: null
  id: resource_b96f7051
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2020_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2019 Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/KWT/kwt_ppp_2019_1km_Aggregated.tif
  format: null
  id: resource_4073e171
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2019_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2019 Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/KWT/kwt_ppp_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_8857f7ff
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/KWT/kwt_ppp_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_f24d3793
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/KWT/kwt_ppp_2019_1km_Aggregated_UNadj.tif
  format: null
  id: resource_6a169d2f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2019_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2018 Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/KWT/kwt_ppp_2018_1km_Aggregated.tif
  format: null
  id: resource_39f0f589
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2018_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2018 Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/KWT/kwt_ppp_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_1c9bca6b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/KWT/kwt_ppp_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_11c7b619
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/KWT/kwt_ppp_2018_1km_Aggregated_UNadj.tif
  format: null
  id: resource_96ddb3e6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2018_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2017 Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/KWT/kwt_ppp_2017_1km_Aggregated.tif
  format: null
  id: resource_6df22619
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2017_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2017 Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/KWT/kwt_ppp_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_64118217
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/KWT/kwt_ppp_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_6c110095
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/KWT/kwt_ppp_2017_1km_Aggregated_UNadj.tif
  format: null
  id: resource_25f4f95f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2017_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2016 Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/KWT/kwt_ppp_2016_1km_Aggregated.tif
  format: null
  id: resource_e2b24479
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2016_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Kuwait - Population Counts (The spatial distribution of population
    in 2016 Kuwait)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/KWT/kwt_ppp_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_5995aec6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/KWT/kwt_ppp_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_5e770a3b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Kuwait
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/KWT/kwt_ppp_2016_1km_Aggregated_UNadj.tif
  format: null
  id: resource_76a21c5a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: kwt_ppp_2016_1km_Aggregated_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-kwt_worldpop_kuwaitpopulationcounts_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - KWT
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Kuwait - Population Counts
version: null
vulnerability: null
---
