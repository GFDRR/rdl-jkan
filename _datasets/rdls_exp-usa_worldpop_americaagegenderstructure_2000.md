---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-united-states-of-america
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-united-states-of-america
dataset_id: rdls_exp-usa_worldpop_americaagegenderstructure_2000
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
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-united-states-of-america]'
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
    et al.) to census and survey population data to produce gridded population counts
    stratified by age group and gender at 100m resolution (3 arc-seconds) for 2020.
    The dataset comprises 180 GeoTIFF files representing population counts for each
    age-gender cohort across the United States.
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-united-states-of-america
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
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_80_2020.tif
  format: null
  id: resource_aabaaea9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_75_2020.tif
  format: null
  id: resource_eb46b91b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_70_2020.tif
  format: null
  id: resource_3d5110ab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_65_2020.tif
  format: null
  id: resource_c83c115e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_60_2020.tif
  format: null
  id: resource_b234ab4f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_5_2020.tif
  format: null
  id: resource_85238154
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_55_2020.tif
  format: null
  id: resource_382e7bb2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_50_2020.tif
  format: null
  id: resource_83655494
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_45_2020.tif
  format: null
  id: resource_c29b04ba
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_40_2020.tif
  format: null
  id: resource_0683591b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_35_2020.tif
  format: null
  id: resource_1c33a599
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_30_2020.tif
  format: null
  id: resource_4bf54779
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_25_2020.tif
  format: null
  id: resource_6cb478f9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_20_2020.tif
  format: null
  id: resource_b691119b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_1_2020.tif
  format: null
  id: resource_2ad6bbf3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_15_2020.tif
  format: null
  id: resource_12717ed7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_10_2020.tif
  format: null
  id: resource_62ae57fb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_m_0_2020.tif
  format: null
  id: resource_902fb76e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_80_2020.tif
  format: null
  id: resource_7faea181
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_75_2020.tif
  format: null
  id: resource_57a76d99
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_70_2020.tif
  format: null
  id: resource_15b42ffe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_65_2020.tif
  format: null
  id: resource_e374a6cf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_60_2020.tif
  format: null
  id: resource_7d800973
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_5_2020.tif
  format: null
  id: resource_73bf99f5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_55_2020.tif
  format: null
  id: resource_a3783ebf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_50_2020.tif
  format: null
  id: resource_b8270a2c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_45_2020.tif
  format: null
  id: resource_3a8df893
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_40_2020.tif
  format: null
  id: resource_561df410
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_35_2020.tif
  format: null
  id: resource_432a4194
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_30_2020.tif
  format: null
  id: resource_c5a71f90
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_25_2020.tif
  format: null
  id: resource_0ed1deea
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_20_2020.tif
  format: null
  id: resource_3ed2c522
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_1_2020.tif
  format: null
  id: resource_bcf00df2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_15_2020.tif
  format: null
  id: resource_099b1290
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_10_2020.tif
  format: null
  id: resource_0c13a031
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/USA/usa_f_0_2020.tif
  format: null
  id: resource_e527ef12
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_80_2019.tif
  format: null
  id: resource_f71904f6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_75_2019.tif
  format: null
  id: resource_b3303b55
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_70_2019.tif
  format: null
  id: resource_16930cf2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_65_2019.tif
  format: null
  id: resource_f1735493
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_60_2019.tif
  format: null
  id: resource_79829ee1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_5_2019.tif
  format: null
  id: resource_3ff424c4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_55_2019.tif
  format: null
  id: resource_226332ae
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_50_2019.tif
  format: null
  id: resource_10d4d26c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_45_2019.tif
  format: null
  id: resource_cccc2100
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_40_2019.tif
  format: null
  id: resource_79935f1d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_35_2019.tif
  format: null
  id: resource_8b606a27
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_30_2019.tif
  format: null
  id: resource_8d7b5aac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_25_2019.tif
  format: null
  id: resource_5f49a577
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_20_2019.tif
  format: null
  id: resource_aa5fb5a7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_1_2019.tif
  format: null
  id: resource_d7baaf0f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_15_2019.tif
  format: null
  id: resource_ffba94dd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_10_2019.tif
  format: null
  id: resource_25c65d4e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_m_0_2019.tif
  format: null
  id: resource_facac147
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_80_2019.tif
  format: null
  id: resource_900505b0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_75_2019.tif
  format: null
  id: resource_706e59e2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_70_2019.tif
  format: null
  id: resource_9c7bfa18
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_65_2019.tif
  format: null
  id: resource_c68e35f0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_60_2019.tif
  format: null
  id: resource_2b93cc0c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_5_2019.tif
  format: null
  id: resource_cefe5127
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_55_2019.tif
  format: null
  id: resource_816525c1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_50_2019.tif
  format: null
  id: resource_38892c78
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_45_2019.tif
  format: null
  id: resource_08bbc704
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_40_2019.tif
  format: null
  id: resource_60b5a9d2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_35_2019.tif
  format: null
  id: resource_6062ff02
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_30_2019.tif
  format: null
  id: resource_b2ee95b3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_25_2019.tif
  format: null
  id: resource_16a38f25
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_20_2019.tif
  format: null
  id: resource_7378f759
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_1_2019.tif
  format: null
  id: resource_c5c4ef7f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_15_2019.tif
  format: null
  id: resource_1f96e037
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_10_2019.tif
  format: null
  id: resource_a02b229e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/USA/usa_f_0_2019.tif
  format: null
  id: resource_9d0533de
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_80_2018.tif
  format: null
  id: resource_6861d031
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_75_2018.tif
  format: null
  id: resource_9fbbbba0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_70_2018.tif
  format: null
  id: resource_f470d7a4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_65_2018.tif
  format: null
  id: resource_6b326de3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_60_2018.tif
  format: null
  id: resource_bce4095b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_5_2018.tif
  format: null
  id: resource_555f073b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_55_2018.tif
  format: null
  id: resource_c3d1c7e8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_50_2018.tif
  format: null
  id: resource_7e7c130c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_45_2018.tif
  format: null
  id: resource_d17f361c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_40_2018.tif
  format: null
  id: resource_ec74345a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_35_2018.tif
  format: null
  id: resource_07dc6096
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_30_2018.tif
  format: null
  id: resource_03a6ae57
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_25_2018.tif
  format: null
  id: resource_2430958a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_20_2018.tif
  format: null
  id: resource_7a9131c5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_1_2018.tif
  format: null
  id: resource_f18f674d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_15_2018.tif
  format: null
  id: resource_33d48d2d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_10_2018.tif
  format: null
  id: resource_ebe66fe8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_m_0_2018.tif
  format: null
  id: resource_0582eacf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_80_2018.tif
  format: null
  id: resource_0c24bedf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_75_2018.tif
  format: null
  id: resource_aa78b49b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_70_2018.tif
  format: null
  id: resource_c4b30af2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_65_2018.tif
  format: null
  id: resource_7ddae70f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_60_2018.tif
  format: null
  id: resource_76e52f4d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_5_2018.tif
  format: null
  id: resource_0c2b32c7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_55_2018.tif
  format: null
  id: resource_86b66845
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_50_2018.tif
  format: null
  id: resource_1f5801bc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_45_2018.tif
  format: null
  id: resource_cf41eb08
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_40_2018.tif
  format: null
  id: resource_640a70d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_35_2018.tif
  format: null
  id: resource_9d7830de
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_30_2018.tif
  format: null
  id: resource_c9973da4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_25_2018.tif
  format: null
  id: resource_0bcc71ae
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_20_2018.tif
  format: null
  id: resource_ac86593f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_1_2018.tif
  format: null
  id: resource_58ce05af
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_15_2018.tif
  format: null
  id: resource_d6bc4c13
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_10_2018.tif
  format: null
  id: resource_636500af
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/USA/usa_f_0_2018.tif
  format: null
  id: resource_9e1afa33
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_80_2017.tif
  format: null
  id: resource_688ac037
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_75_2017.tif
  format: null
  id: resource_3d15ea73
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_70_2017.tif
  format: null
  id: resource_334822b5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_65_2017.tif
  format: null
  id: resource_e4dd1244
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_60_2017.tif
  format: null
  id: resource_d00c9c28
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_5_2017.tif
  format: null
  id: resource_4d08100c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_55_2017.tif
  format: null
  id: resource_f5739d09
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_50_2017.tif
  format: null
  id: resource_3e417d27
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_45_2017.tif
  format: null
  id: resource_9cbf8e77
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_40_2017.tif
  format: null
  id: resource_726bfd3f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_35_2017.tif
  format: null
  id: resource_34702116
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_30_2017.tif
  format: null
  id: resource_e0d0a052
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_25_2017.tif
  format: null
  id: resource_9ab7429c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_20_2017.tif
  format: null
  id: resource_b315ee92
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_1_2017.tif
  format: null
  id: resource_4b2e0dd6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_15_2017.tif
  format: null
  id: resource_40cd06fb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_10_2017.tif
  format: null
  id: resource_ad6334d0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_m_0_2017.tif
  format: null
  id: resource_765eada6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_80_2017.tif
  format: null
  id: resource_acc0c655
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_75_2017.tif
  format: null
  id: resource_aec5c9bc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_70_2017.tif
  format: null
  id: resource_c81a8544
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_65_2017.tif
  format: null
  id: resource_84ff6987
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_60_2017.tif
  format: null
  id: resource_0e044974
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_5_2017.tif
  format: null
  id: resource_a9422c01
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_55_2017.tif
  format: null
  id: resource_e81748e8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_50_2017.tif
  format: null
  id: resource_96be09ae
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_45_2017.tif
  format: null
  id: resource_db07db11
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_40_2017.tif
  format: null
  id: resource_ad2f363f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_35_2017.tif
  format: null
  id: resource_a3738434
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_30_2017.tif
  format: null
  id: resource_213c740d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_25_2017.tif
  format: null
  id: resource_5fd10819
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_20_2017.tif
  format: null
  id: resource_48ff529e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_1_2017.tif
  format: null
  id: resource_e79b54be
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_15_2017.tif
  format: null
  id: resource_41bab7bf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_10_2017.tif
  format: null
  id: resource_547eb2a8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/USA/usa_f_0_2017.tif
  format: null
  id: resource_28d0293e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_80_2016.tif
  format: null
  id: resource_f90feb15
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_75_2016.tif
  format: null
  id: resource_acf2ec43
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_70_2016.tif
  format: null
  id: resource_79999027
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_65_2016.tif
  format: null
  id: resource_bcb3b32a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_60_2016.tif
  format: null
  id: resource_29712ea2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_5_2016.tif
  format: null
  id: resource_e1cf5664
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_55_2016.tif
  format: null
  id: resource_2784da7c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_50_2016.tif
  format: null
  id: resource_27da6338
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_45_2016.tif
  format: null
  id: resource_550ffebd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_40_2016.tif
  format: null
  id: resource_3e5b6884
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_35_2016.tif
  format: null
  id: resource_7d08e59c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_30_2016.tif
  format: null
  id: resource_341a49c3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_25_2016.tif
  format: null
  id: resource_573b02ff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_20_2016.tif
  format: null
  id: resource_84385360
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_1_2016.tif
  format: null
  id: resource_2d264f87
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_15_2016.tif
  format: null
  id: resource_492eaa58
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_10_2016.tif
  format: null
  id: resource_66696eb5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_m_0_2016.tif
  format: null
  id: resource_4cc2b45d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_m_0_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_80_2016.tif
  format: null
  id: resource_6b674324
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_75_2016.tif
  format: null
  id: resource_85748b14
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_70_2016.tif
  format: null
  id: resource_3bb81af4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_65_2016.tif
  format: null
  id: resource_e0679288
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_60_2016.tif
  format: null
  id: resource_0fae765e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_5_2016.tif
  format: null
  id: resource_1802cbcf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_55_2016.tif
  format: null
  id: resource_b15822b8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_50_2016.tif
  format: null
  id: resource_2aa640eb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_45_2016.tif
  format: null
  id: resource_4be96c6b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_40_2016.tif
  format: null
  id: resource_865992fc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_35_2016.tif
  format: null
  id: resource_433019f9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_30_2016.tif
  format: null
  id: resource_3f151989
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_25_2016.tif
  format: null
  id: resource_c7baaee3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_20_2016.tif
  format: null
  id: resource_e608263d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_1_2016.tif
  format: null
  id: resource_7aff4136
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_15_2016.tif
  format: null
  id: resource_2952f6e3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_10_2016.tif
  format: null
  id: resource_a60a547b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: United States of America 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/USA/usa_f_0_2016.tif
  format: null
  id: resource_9703fd42
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: usa_f_0_2016.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-usa_worldpop_americaagegenderstructure_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - USA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: United States of America - Age and gender structures
version: null
vulnerability: null
---
