---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop, University of Southampton, UK
    url: https://data.humdata.org/dataset/worldpop-population-counts-for-malaysia
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-malaysia
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-for-malaysia
dataset_id: rdls_exp-mys_worldpop_populationcounts_2000
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
  Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-for-malaysia]'
details: null
exposure:
- asset_type:
    description: Gridded population counts at 100m resolution for Malaysia, adjusted
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
  description: WorldPop produced gridded population estimates for Malaysia using country-specific
    customized methods, with outputs available at 100m resolution in multiple variants
    (UN-adjusted and constrained). Data were aggregated to 1km resolution and provided
    in GeoTIFF and ASCII XYZ formats with geographic coordinates in WGS84, with country
    totals calibrated to official national population figures.
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-for-malaysia
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
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2020, Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/MYS/mys_ppp_2020.tif
  format: null
  id: resource_e0003d58
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2019, Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/MYS/mys_ppp_2019.tif
  format: null
  id: resource_1c35abd8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2018, Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/MYS/mys_ppp_2018.tif
  format: null
  id: resource_f1252f76
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2017, Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/MYS/mys_ppp_2017.tif
  format: null
  id: resource_50ceadf3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2016, Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/MYS/mys_ppp_2016.tif
  format: null
  id: resource_f3d3bcad
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2020/MYS/mys_ppp_2020_UNadj.tif
  format: null
  id: resource_36d43f51
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2020_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2019/MYS/mys_ppp_2019_UNadj.tif
  format: null
  id: resource_5db92633
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2019_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2018/MYS/mys_ppp_2018_UNadj.tif
  format: null
  id: resource_e9d10415
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2018_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2017/MYS/mys_ppp_2017_UNadj.tif
  format: null
  id: resource_bcab538e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2017_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020/2016/MYS/mys_ppp_2016_UNadj.tif
  format: null
  id: resource_edddd387
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2016_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2020, Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/MYS/mys_ppp_2020_constrained.tif
  format: null
  id: resource_5d473134
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2020_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_Constrained/2020/BSGM/MYS/mys_ppp_2020_UNadj_constrained.tif
  format: null
  id: resource_1dae7a6c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2020_UNadj_constrained.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2020 Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/MYS/mys_ppp_2020_1km_Aggregated.tif
  format: null
  id: resource_e14f1de2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2020_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2020 Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2020/MYS/mys_ppp_2020_1km_ASCII_XYZ.zip
  format: null
  id: resource_5050ef0e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2020_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/MYS/mys_ppp_2020_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_aab41215
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2020_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2020 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2020/MYS/mys_ppp_2020_1km_Aggregated_UNadj.tif
  format: null
  id: resource_c21d70ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2020_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2019 Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/MYS/mys_ppp_2019_1km_Aggregated.tif
  format: null
  id: resource_0774ef28
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2019_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2019 Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2019/MYS/mys_ppp_2019_1km_ASCII_XYZ.zip
  format: null
  id: resource_a5a1f836
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2019_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/MYS/mys_ppp_2019_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_e986ec25
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2019_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2019 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2019/MYS/mys_ppp_2019_1km_Aggregated_UNadj.tif
  format: null
  id: resource_494315f5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2019_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2018 Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/MYS/mys_ppp_2018_1km_Aggregated.tif
  format: null
  id: resource_4bb1902e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2018_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2018 Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2018/MYS/mys_ppp_2018_1km_ASCII_XYZ.zip
  format: null
  id: resource_1b9a3246
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2018_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/MYS/mys_ppp_2018_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_b5bba4c1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2018_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2018 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2018/MYS/mys_ppp_2018_1km_Aggregated_UNadj.tif
  format: null
  id: resource_b718c64f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2018_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2017 Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/MYS/mys_ppp_2017_1km_Aggregated.tif
  format: null
  id: resource_dbe9d020
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2017_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2017 Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2017/MYS/mys_ppp_2017_1km_ASCII_XYZ.zip
  format: null
  id: resource_04ede236
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2017_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/MYS/mys_ppp_2017_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_7cc0836b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2017_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2017 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2017/MYS/mys_ppp_2017_1km_Aggregated_UNadj.tif
  format: null
  id: resource_7f698e87
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2017_1km_Aggregated_UNadj.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2016 Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/MYS/mys_ppp_2016_1km_Aggregated.tif
  format: null
  id: resource_9b72b9c0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2016_1km_Aggregated.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Malaysia - Population Counts (The spatial distribution of population
    in 2016 Malaysia)
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km/2016/MYS/mys_ppp_2016_1km_ASCII_XYZ.zip
  format: null
  id: resource_c3dc1b71
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2016_1km_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/MYS/mys_ppp_2016_1km_UNadj_ASCII_XYZ.zip
  format: null
  id: resource_99fa0967
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2016_1km_UNadj_ASCII_XYZ.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: The spatial distribution of population in 2016 with country total adjusted
    to match the corresponding UNPD estimate, Malaysia
  download_url: https://data.worldpop.org/GIS/Population/Global_2000_2020_1km_UNadj/2016/MYS/mys_ppp_2016_1km_Aggregated_UNadj.tif
  format: null
  id: resource_6fba8165
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mys_ppp_2016_1km_Aggregated_UNadj.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mys_worldpop_populationcounts_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - MYS
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Malaysia - Population Counts
version: null
vulnerability: null
---
