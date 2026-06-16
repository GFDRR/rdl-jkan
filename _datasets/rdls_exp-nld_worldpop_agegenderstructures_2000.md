---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-netherlands
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-netherlands
dataset_id: rdls_exp-nld_worldpop_agegenderstructures_2000
description: 'WorldPop produces different types of gridded population count datasets,
  depending on the methods used and end application. Please make sure you have read
  our Mapping Populations overview page before choosing and downloading a dataset.
  A description of the modelling methods used for age and gender structures can be
  found in Tatem et al and Pezzulo et al . Details of the input population count datasets
  used can be found here , and age/gender structure proportion datasets here . Both
  top-down ''unconstrained'' and ''constrained'' versions of the datasets are available,
  and the differences between the two methods are outlined here . The datasets represent
  the outputs from a project focused on construction of consistent 100m resolution
  population count datasets for all countries of the World structured by male/female
  and 5-year age classes (plus a <1 year class). These efforts necessarily involved
  some shortcuts for consistency. The unconstrained datasets are available for each
  year from 2000 to 2020. The constrained datasets are only available for 2020 at
  present, given the time periods represented by the building footprint and built
  settlement datasets used in the mapping. Data for earlier dates is available directly
  from WorldPop. WorldPop (www.worldpop.org - School of Geography and Environmental
  Science, University of Southampton; Department of Geography and Geosciences, University
  of Louisville; Departement de Geographie, Universite de Namur) and Center for International
  Earth Science Information Network (CIESIN), Columbia University (2018). Global High
  Resolution Population Denominators Project - Funded by The Bill and Melinda Gates
  Foundation (OPP1134076). https://dx.doi.org/10.5258/SOTON/WP00646. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-netherlands]'
details: null
exposure:
- asset_type:
    description: Gridded population counts disaggregated by age group (0-1, 5-year
      intervals to 80+) and gender for 2020
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
  description: WorldPop applied spatial disaggregation methods (Tatem et al., Pezzulo
    et al.) to census and survey population data to produce gridded estimates of population
    counts by age group and gender at 100m resolution (3 arc-seconds) for the Netherlands
    in 2020, delivered as separate GeoTIFF rasters per demographic category.
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-netherlands
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_80_2020.tif
  format: null
  id: resource_04252f0e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_75_2020.tif
  format: null
  id: resource_d44a4b2c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_70_2020.tif
  format: null
  id: resource_af1a9b2c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_65_2020.tif
  format: null
  id: resource_56d9f4c5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_60_2020.tif
  format: null
  id: resource_c1ebd5e3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_5_2020.tif
  format: null
  id: resource_c354e0a1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_55_2020.tif
  format: null
  id: resource_2507b9c0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_50_2020.tif
  format: null
  id: resource_730afc18
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_45_2020.tif
  format: null
  id: resource_6e6b714c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_40_2020.tif
  format: null
  id: resource_dbe299a4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_35_2020.tif
  format: null
  id: resource_fa101834
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_30_2020.tif
  format: null
  id: resource_c9764b06
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_25_2020.tif
  format: null
  id: resource_fe8bac7d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_20_2020.tif
  format: null
  id: resource_b215b491
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_1_2020.tif
  format: null
  id: resource_dd91e78f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_15_2020.tif
  format: null
  id: resource_747609d1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_10_2020.tif
  format: null
  id: resource_764c50b8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_m_0_2020.tif
  format: null
  id: resource_b7b630de
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_80_2020.tif
  format: null
  id: resource_f0df2fbc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_75_2020.tif
  format: null
  id: resource_bd1c75cc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_70_2020.tif
  format: null
  id: resource_b6f3a187
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_65_2020.tif
  format: null
  id: resource_806c0c3c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_60_2020.tif
  format: null
  id: resource_9e791669
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_5_2020.tif
  format: null
  id: resource_28f2e8d8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_55_2020.tif
  format: null
  id: resource_59aa476e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_50_2020.tif
  format: null
  id: resource_2bf50ba2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_45_2020.tif
  format: null
  id: resource_9dc0e0ee
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_40_2020.tif
  format: null
  id: resource_0f1acf4e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_35_2020.tif
  format: null
  id: resource_1378ff90
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_30_2020.tif
  format: null
  id: resource_53d4cbdf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_25_2020.tif
  format: null
  id: resource_6c914039
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_20_2020.tif
  format: null
  id: resource_99d3d651
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_1_2020.tif
  format: null
  id: resource_c9e0d29a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_15_2020.tif
  format: null
  id: resource_3effb133
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_10_2020.tif
  format: null
  id: resource_e526492b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NLD/nld_f_0_2020.tif
  format: null
  id: resource_5b386f8a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_80_2019.tif
  format: null
  id: resource_49ca8685
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_75_2019.tif
  format: null
  id: resource_f689ed8a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_70_2019.tif
  format: null
  id: resource_908e2472
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_65_2019.tif
  format: null
  id: resource_74fde97c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_60_2019.tif
  format: null
  id: resource_f35d67c3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_5_2019.tif
  format: null
  id: resource_d0a8517a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_55_2019.tif
  format: null
  id: resource_c80fe08e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_50_2019.tif
  format: null
  id: resource_685d5a15
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_45_2019.tif
  format: null
  id: resource_4392df13
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_40_2019.tif
  format: null
  id: resource_7489d70c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_35_2019.tif
  format: null
  id: resource_1d4d16fb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_30_2019.tif
  format: null
  id: resource_45085e53
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_25_2019.tif
  format: null
  id: resource_ae5e8696
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_20_2019.tif
  format: null
  id: resource_e53d546e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_1_2019.tif
  format: null
  id: resource_970f7609
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_15_2019.tif
  format: null
  id: resource_2e6cedcd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_10_2019.tif
  format: null
  id: resource_7a9d9371
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_m_0_2019.tif
  format: null
  id: resource_a33d0efe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_80_2019.tif
  format: null
  id: resource_7e2e88ea
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_75_2019.tif
  format: null
  id: resource_d7fd5986
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_70_2019.tif
  format: null
  id: resource_e2fe22ce
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_65_2019.tif
  format: null
  id: resource_7e97ad06
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_60_2019.tif
  format: null
  id: resource_64913906
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_5_2019.tif
  format: null
  id: resource_927a43da
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_55_2019.tif
  format: null
  id: resource_86c2d0df
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_50_2019.tif
  format: null
  id: resource_d248dff3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_45_2019.tif
  format: null
  id: resource_4220426e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_40_2019.tif
  format: null
  id: resource_4a53cdbe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_35_2019.tif
  format: null
  id: resource_846c6897
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_30_2019.tif
  format: null
  id: resource_ab021efc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_25_2019.tif
  format: null
  id: resource_c8f05eac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_20_2019.tif
  format: null
  id: resource_c36ebb9a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_1_2019.tif
  format: null
  id: resource_4caa6d4c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_15_2019.tif
  format: null
  id: resource_b63381b3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_10_2019.tif
  format: null
  id: resource_8fd65778
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NLD/nld_f_0_2019.tif
  format: null
  id: resource_075f7cf1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_80_2018.tif
  format: null
  id: resource_fb0e4437
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_75_2018.tif
  format: null
  id: resource_eb3ddafa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_70_2018.tif
  format: null
  id: resource_ae6c523b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_65_2018.tif
  format: null
  id: resource_aad0c0d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_60_2018.tif
  format: null
  id: resource_656a3cc5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_5_2018.tif
  format: null
  id: resource_e23311ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_55_2018.tif
  format: null
  id: resource_3d3fcffe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_50_2018.tif
  format: null
  id: resource_a8df68a7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_45_2018.tif
  format: null
  id: resource_7ec693ae
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_40_2018.tif
  format: null
  id: resource_54fd7dc4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_35_2018.tif
  format: null
  id: resource_ca2addd8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_30_2018.tif
  format: null
  id: resource_158b46d6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_25_2018.tif
  format: null
  id: resource_2bc652d2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_20_2018.tif
  format: null
  id: resource_97268069
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_1_2018.tif
  format: null
  id: resource_dd918bbb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_15_2018.tif
  format: null
  id: resource_225421ce
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_10_2018.tif
  format: null
  id: resource_0418c02c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_m_0_2018.tif
  format: null
  id: resource_7a77aa54
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_80_2018.tif
  format: null
  id: resource_75014465
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_75_2018.tif
  format: null
  id: resource_a3cdebc0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_70_2018.tif
  format: null
  id: resource_2d64dd18
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_65_2018.tif
  format: null
  id: resource_95663851
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_60_2018.tif
  format: null
  id: resource_b808e02b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_5_2018.tif
  format: null
  id: resource_24df7d55
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_55_2018.tif
  format: null
  id: resource_ca42ddf2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_50_2018.tif
  format: null
  id: resource_0d54ad2d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_45_2018.tif
  format: null
  id: resource_8e8c5474
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_40_2018.tif
  format: null
  id: resource_f5e485a8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_35_2018.tif
  format: null
  id: resource_e67341fb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_30_2018.tif
  format: null
  id: resource_d62798ec
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_25_2018.tif
  format: null
  id: resource_4b2b1612
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_20_2018.tif
  format: null
  id: resource_19a93d27
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_1_2018.tif
  format: null
  id: resource_8b8fdd72
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_15_2018.tif
  format: null
  id: resource_fd7e6f7d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_10_2018.tif
  format: null
  id: resource_2b8da4c5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NLD/nld_f_0_2018.tif
  format: null
  id: resource_66efc264
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_80_2017.tif
  format: null
  id: resource_43efe725
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_75_2017.tif
  format: null
  id: resource_d81bb7fd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_70_2017.tif
  format: null
  id: resource_3e55878c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_65_2017.tif
  format: null
  id: resource_c34f6da2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_60_2017.tif
  format: null
  id: resource_84ee1f3b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_5_2017.tif
  format: null
  id: resource_5c0f50b8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_55_2017.tif
  format: null
  id: resource_85ab1031
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_50_2017.tif
  format: null
  id: resource_0c388cc7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_45_2017.tif
  format: null
  id: resource_8698bd0c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_40_2017.tif
  format: null
  id: resource_f55320f0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_35_2017.tif
  format: null
  id: resource_372e777f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_30_2017.tif
  format: null
  id: resource_908622f5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_25_2017.tif
  format: null
  id: resource_ab964bca
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_20_2017.tif
  format: null
  id: resource_b4bb66da
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_1_2017.tif
  format: null
  id: resource_fb084002
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_15_2017.tif
  format: null
  id: resource_36fa971e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_10_2017.tif
  format: null
  id: resource_552533c1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_m_0_2017.tif
  format: null
  id: resource_5ff8782b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_80_2017.tif
  format: null
  id: resource_4a20d566
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_75_2017.tif
  format: null
  id: resource_6ff8d8e1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_70_2017.tif
  format: null
  id: resource_007ab263
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_65_2017.tif
  format: null
  id: resource_d25b5a09
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_60_2017.tif
  format: null
  id: resource_502b870d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_5_2017.tif
  format: null
  id: resource_7aee5328
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_55_2017.tif
  format: null
  id: resource_df437331
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_50_2017.tif
  format: null
  id: resource_20f0e701
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_45_2017.tif
  format: null
  id: resource_a12074cf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_40_2017.tif
  format: null
  id: resource_d798bf43
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_35_2017.tif
  format: null
  id: resource_328e5f92
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_30_2017.tif
  format: null
  id: resource_cfcb93c5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_25_2017.tif
  format: null
  id: resource_45c3b874
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_20_2017.tif
  format: null
  id: resource_20554cff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_1_2017.tif
  format: null
  id: resource_3aa5bfc7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_15_2017.tif
  format: null
  id: resource_8ac04f72
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_10_2017.tif
  format: null
  id: resource_1b76ba05
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NLD/nld_f_0_2017.tif
  format: null
  id: resource_de3ecd24
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_80_2016.tif
  format: null
  id: resource_088cc700
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_75_2016.tif
  format: null
  id: resource_8195c418
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_70_2016.tif
  format: null
  id: resource_34d005e9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_65_2016.tif
  format: null
  id: resource_ed9f1047
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_60_2016.tif
  format: null
  id: resource_7469f0de
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_5_2016.tif
  format: null
  id: resource_147150dd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_55_2016.tif
  format: null
  id: resource_19bdbfe5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_50_2016.tif
  format: null
  id: resource_bbd3c1fb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_45_2016.tif
  format: null
  id: resource_ad00981a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_40_2016.tif
  format: null
  id: resource_e1e5077f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_35_2016.tif
  format: null
  id: resource_617a2d69
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_30_2016.tif
  format: null
  id: resource_990c9ce5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_25_2016.tif
  format: null
  id: resource_e5be97bf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_20_2016.tif
  format: null
  id: resource_8d0322ad
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_1_2016.tif
  format: null
  id: resource_81bea247
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_15_2016.tif
  format: null
  id: resource_c208c95a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_10_2016.tif
  format: null
  id: resource_3f7d10a4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_m_0_2016.tif
  format: null
  id: resource_65be7cb7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_m_0_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_80_2016.tif
  format: null
  id: resource_267ea51b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_75_2016.tif
  format: null
  id: resource_769325ae
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_70_2016.tif
  format: null
  id: resource_548d6452
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_65_2016.tif
  format: null
  id: resource_1109e5e6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_60_2016.tif
  format: null
  id: resource_66b671fb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_5_2016.tif
  format: null
  id: resource_5494e95e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_55_2016.tif
  format: null
  id: resource_c6eae191
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_50_2016.tif
  format: null
  id: resource_4932f4c1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_45_2016.tif
  format: null
  id: resource_33918e5b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_40_2016.tif
  format: null
  id: resource_0954bdc9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_35_2016.tif
  format: null
  id: resource_6a0d1a70
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_30_2016.tif
  format: null
  id: resource_32707a75
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_25_2016.tif
  format: null
  id: resource_1005455c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_20_2016.tif
  format: null
  id: resource_63e021bb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_1_2016.tif
  format: null
  id: resource_d418b740
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_15_2016.tif
  format: null
  id: resource_f21128d8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_10_2016.tif
  format: null
  id: resource_64bf60e1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Netherlands - Age and gender structures (Netherlands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NLD/nld_f_0_2016.tif
  format: null
  id: resource_a3e0f115
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: nld_f_0_2016.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-nld_worldpop_agegenderstructures_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - NLD
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Netherlands - Age and gender structures
version: null
vulnerability: null
---
