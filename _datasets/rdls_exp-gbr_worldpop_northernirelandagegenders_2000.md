---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-united-kingdom-of-great-britain-and-northern-ireland
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-united-kingdom-of-great-britain-and-northern-ireland
dataset_id: rdls_exp-gbr_worldpop_northernirelandagegenders_2000
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
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-united-kingdom-of-great-britain-and-northern-ireland]'
details: null
exposure:
- asset_type:
    description: Gridded population counts disaggregated by age group (0-1, 5-year
      bands to 80+) and gender for 2020
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
  description: WorldPop generated gridded population estimates for the UK at 100m
    resolution by disaggregating baseline population counts by age group and gender
    using statistical modeling methods described in Tatem et al. and Pezzulo et al.,
    producing 180 separate GeoTIFF rasters representing population density for each
    age-gender cohort in 2020.
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-united-kingdom-of-great-britain-and-northern-ireland
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
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_80_2020.tif
  format: null
  id: resource_2affa80c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_75_2020.tif
  format: null
  id: resource_23736811
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_70_2020.tif
  format: null
  id: resource_3cf851fa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_65_2020.tif
  format: null
  id: resource_f72747ff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_60_2020.tif
  format: null
  id: resource_04030e39
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_5_2020.tif
  format: null
  id: resource_2437b40e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_55_2020.tif
  format: null
  id: resource_affe2eb2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_50_2020.tif
  format: null
  id: resource_84ad5dec
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_45_2020.tif
  format: null
  id: resource_28ec880d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_40_2020.tif
  format: null
  id: resource_ce2ee922
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_35_2020.tif
  format: null
  id: resource_1519f349
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_30_2020.tif
  format: null
  id: resource_1e7661a9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_25_2020.tif
  format: null
  id: resource_49f8e4f1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_20_2020.tif
  format: null
  id: resource_6be13eff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_1_2020.tif
  format: null
  id: resource_495ee0a5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_15_2020.tif
  format: null
  id: resource_ebb8c9b8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_10_2020.tif
  format: null
  id: resource_73c1d55e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_m_0_2020.tif
  format: null
  id: resource_880af3bb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_80_2020.tif
  format: null
  id: resource_71d932a3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_75_2020.tif
  format: null
  id: resource_9c7db606
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_70_2020.tif
  format: null
  id: resource_b4a276b8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_65_2020.tif
  format: null
  id: resource_68a9e012
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_60_2020.tif
  format: null
  id: resource_eecb6b7a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_5_2020.tif
  format: null
  id: resource_60c46dc9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_55_2020.tif
  format: null
  id: resource_2fe82721
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_50_2020.tif
  format: null
  id: resource_3c80db43
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_45_2020.tif
  format: null
  id: resource_84adf23c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_40_2020.tif
  format: null
  id: resource_66ca260b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_35_2020.tif
  format: null
  id: resource_eda3e53a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_30_2020.tif
  format: null
  id: resource_9129c894
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_25_2020.tif
  format: null
  id: resource_72dab5c2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_20_2020.tif
  format: null
  id: resource_9ead288a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_1_2020.tif
  format: null
  id: resource_0ae08c4d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_15_2020.tif
  format: null
  id: resource_30ab6899
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_10_2020.tif
  format: null
  id: resource_5cea6a84
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GBR/gbr_f_0_2020.tif
  format: null
  id: resource_9653309e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_80_2019.tif
  format: null
  id: resource_63487151
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_75_2019.tif
  format: null
  id: resource_21c9767b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_70_2019.tif
  format: null
  id: resource_79bbcaf8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_65_2019.tif
  format: null
  id: resource_5d6e8507
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_60_2019.tif
  format: null
  id: resource_c2e48b44
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_5_2019.tif
  format: null
  id: resource_7428d378
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_55_2019.tif
  format: null
  id: resource_b61a213e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_50_2019.tif
  format: null
  id: resource_92b70284
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_45_2019.tif
  format: null
  id: resource_fedb761d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_40_2019.tif
  format: null
  id: resource_22cd28a4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_35_2019.tif
  format: null
  id: resource_b23336b4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_30_2019.tif
  format: null
  id: resource_1ee30094
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_25_2019.tif
  format: null
  id: resource_3d97df5e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_20_2019.tif
  format: null
  id: resource_fb82b083
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_1_2019.tif
  format: null
  id: resource_1f19917a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_15_2019.tif
  format: null
  id: resource_33f1bec5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_10_2019.tif
  format: null
  id: resource_c0d6a340
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_m_0_2019.tif
  format: null
  id: resource_5041de1d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_80_2019.tif
  format: null
  id: resource_7ba55a91
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_75_2019.tif
  format: null
  id: resource_ceacc082
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_70_2019.tif
  format: null
  id: resource_9a665035
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_65_2019.tif
  format: null
  id: resource_cb5b53dd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_60_2019.tif
  format: null
  id: resource_8a5b35bb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_5_2019.tif
  format: null
  id: resource_fa752134
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_55_2019.tif
  format: null
  id: resource_10504279
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_50_2019.tif
  format: null
  id: resource_eaa01535
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_45_2019.tif
  format: null
  id: resource_a317b8d2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_40_2019.tif
  format: null
  id: resource_52a5a840
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_35_2019.tif
  format: null
  id: resource_5fae80e8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_30_2019.tif
  format: null
  id: resource_e78a8677
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_25_2019.tif
  format: null
  id: resource_b8bcff29
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_20_2019.tif
  format: null
  id: resource_4ce9cf76
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_1_2019.tif
  format: null
  id: resource_2d69b6fd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_15_2019.tif
  format: null
  id: resource_e0ff6dcc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_10_2019.tif
  format: null
  id: resource_526f82ab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GBR/gbr_f_0_2019.tif
  format: null
  id: resource_836c0316
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_80_2018.tif
  format: null
  id: resource_d1869a94
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_75_2018.tif
  format: null
  id: resource_4da872d2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_70_2018.tif
  format: null
  id: resource_dbb50a4e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_65_2018.tif
  format: null
  id: resource_6520380f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_60_2018.tif
  format: null
  id: resource_248072e8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_5_2018.tif
  format: null
  id: resource_e3c45fcf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_55_2018.tif
  format: null
  id: resource_1916f26e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_50_2018.tif
  format: null
  id: resource_a9e9fd07
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_45_2018.tif
  format: null
  id: resource_d555620c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_40_2018.tif
  format: null
  id: resource_ef8cca9f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_35_2018.tif
  format: null
  id: resource_efd17bf4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_30_2018.tif
  format: null
  id: resource_f3d877ee
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_25_2018.tif
  format: null
  id: resource_ca26493a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_20_2018.tif
  format: null
  id: resource_4639c54b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_1_2018.tif
  format: null
  id: resource_aae88849
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_15_2018.tif
  format: null
  id: resource_d196a575
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_10_2018.tif
  format: null
  id: resource_6d9b8751
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_m_0_2018.tif
  format: null
  id: resource_52c76f11
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_80_2018.tif
  format: null
  id: resource_3a44770e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_75_2018.tif
  format: null
  id: resource_da55e75e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_70_2018.tif
  format: null
  id: resource_ed3bda4e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_65_2018.tif
  format: null
  id: resource_15784a0f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_60_2018.tif
  format: null
  id: resource_80435544
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_5_2018.tif
  format: null
  id: resource_8df4cb47
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_55_2018.tif
  format: null
  id: resource_0d2ffa9e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_50_2018.tif
  format: null
  id: resource_e4a22996
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_45_2018.tif
  format: null
  id: resource_17f2fe73
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_40_2018.tif
  format: null
  id: resource_eb0d2212
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_35_2018.tif
  format: null
  id: resource_a7712ff8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_30_2018.tif
  format: null
  id: resource_f8de9fbc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_25_2018.tif
  format: null
  id: resource_fe392e0f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_20_2018.tif
  format: null
  id: resource_66e8ed78
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_1_2018.tif
  format: null
  id: resource_643ab354
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_15_2018.tif
  format: null
  id: resource_5171a7c6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_10_2018.tif
  format: null
  id: resource_dd584060
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GBR/gbr_f_0_2018.tif
  format: null
  id: resource_8947e2b0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_80_2017.tif
  format: null
  id: resource_bd1a238f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_75_2017.tif
  format: null
  id: resource_dbb87dce
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_70_2017.tif
  format: null
  id: resource_8a7ce813
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_65_2017.tif
  format: null
  id: resource_c743bed4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_60_2017.tif
  format: null
  id: resource_2110e15c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_5_2017.tif
  format: null
  id: resource_e07c546e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_55_2017.tif
  format: null
  id: resource_dbab6ef5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_50_2017.tif
  format: null
  id: resource_c1351a28
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_45_2017.tif
  format: null
  id: resource_333e6f32
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_40_2017.tif
  format: null
  id: resource_b9dda0ee
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_35_2017.tif
  format: null
  id: resource_d8ba218e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_30_2017.tif
  format: null
  id: resource_46bebea9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_25_2017.tif
  format: null
  id: resource_e85feefb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_20_2017.tif
  format: null
  id: resource_d974327a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_1_2017.tif
  format: null
  id: resource_32cc864e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_15_2017.tif
  format: null
  id: resource_8c672ba1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_10_2017.tif
  format: null
  id: resource_b48cb39e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_m_0_2017.tif
  format: null
  id: resource_faf8e8eb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_80_2017.tif
  format: null
  id: resource_4fbbf48f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_75_2017.tif
  format: null
  id: resource_dde6269b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_70_2017.tif
  format: null
  id: resource_e3f6bfb2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_65_2017.tif
  format: null
  id: resource_f8a661d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_60_2017.tif
  format: null
  id: resource_512e4809
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_5_2017.tif
  format: null
  id: resource_60c705d2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_55_2017.tif
  format: null
  id: resource_27623314
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_50_2017.tif
  format: null
  id: resource_8cf81487
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_45_2017.tif
  format: null
  id: resource_409b0852
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_40_2017.tif
  format: null
  id: resource_f7f3179e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_35_2017.tif
  format: null
  id: resource_3b1e4f98
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_30_2017.tif
  format: null
  id: resource_0d8f9872
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_25_2017.tif
  format: null
  id: resource_54909aee
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_20_2017.tif
  format: null
  id: resource_99cc1b4d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_1_2017.tif
  format: null
  id: resource_ee824281
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_15_2017.tif
  format: null
  id: resource_e9aa0dd3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_10_2017.tif
  format: null
  id: resource_cf09255d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GBR/gbr_f_0_2017.tif
  format: null
  id: resource_9b5c6392
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_80_2016.tif
  format: null
  id: resource_103d8201
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_75_2016.tif
  format: null
  id: resource_5da454b5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_70_2016.tif
  format: null
  id: resource_4f3cc1c8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_65_2016.tif
  format: null
  id: resource_9ebeb0d6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_60_2016.tif
  format: null
  id: resource_42755cda
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_5_2016.tif
  format: null
  id: resource_e6ee1044
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_55_2016.tif
  format: null
  id: resource_666ca8dd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_50_2016.tif
  format: null
  id: resource_a9f9aad9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_45_2016.tif
  format: null
  id: resource_ca0687aa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_40_2016.tif
  format: null
  id: resource_11ddce34
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_35_2016.tif
  format: null
  id: resource_4958b81b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_30_2016.tif
  format: null
  id: resource_4d1331d1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_25_2016.tif
  format: null
  id: resource_961c6238
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_20_2016.tif
  format: null
  id: resource_86cb88eb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_1_2016.tif
  format: null
  id: resource_20bbfbd5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_15_2016.tif
  format: null
  id: resource_845a4759
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_10_2016.tif
  format: null
  id: resource_ff39405c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_m_0_2016.tif
  format: null
  id: resource_fa345f57
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_m_0_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_80_2016.tif
  format: null
  id: resource_570c2ba3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_75_2016.tif
  format: null
  id: resource_d2d1e151
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_70_2016.tif
  format: null
  id: resource_54b67671
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_65_2016.tif
  format: null
  id: resource_4af4d5ec
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_60_2016.tif
  format: null
  id: resource_0cf2e592
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_5_2016.tif
  format: null
  id: resource_e60d8541
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_55_2016.tif
  format: null
  id: resource_999b96f5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_50_2016.tif
  format: null
  id: resource_363e42b7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_45_2016.tif
  format: null
  id: resource_04857e00
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_40_2016.tif
  format: null
  id: resource_d7002a65
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_35_2016.tif
  format: null
  id: resource_3d63f627
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_30_2016.tif
  format: null
  id: resource_cf0e5a91
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_25_2016.tif
  format: null
  id: resource_82755d66
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_20_2016.tif
  format: null
  id: resource_d0dbdc45
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_1_2016.tif
  format: null
  id: resource_f06685e1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_15_2016.tif
  format: null
  id: resource_3d3734df
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_10_2016.tif
  format: null
  id: resource_ce8997a0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United Kingdom of Great Britain & Northern Ireland 100m Age structures
    in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GBR/gbr_f_0_2016.tif
  format: null
  id: resource_071b85a1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: gbr_f_0_2016.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-gbr_worldpop_northernirelandagegenders_2000
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
title: United Kingdom of Great Britain and Northern Ireland - Age and gender structures
version: null
vulnerability: null
---
