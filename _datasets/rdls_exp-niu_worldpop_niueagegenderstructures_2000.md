---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-niue
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-niue
dataset_id: rdls_exp-niu_worldpop_niueagegenderstructures_2000
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
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-niue]'
details: null
exposure:
- asset_type:
    description: Gridded population counts disaggregated by age group (0-1, 5-year
      intervals to 80+) and gender for Niue in 2020
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
  description: WorldPop generated gridded population estimates for Niue by disaggregating
    baseline population counts into age groups (0-1, 5-year intervals to 80+) and
    gender using demographic modeling methods (Tatem et al., Pezzulo et al.). The
    resulting rasters at 3 arc-second resolution (~100m) represent estimated population
    density per grid cell for each demographic category in 2020.
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-niue
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
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_80_2020.tif
  format: null
  id: resource_50ae0c84
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_75_2020.tif
  format: null
  id: resource_1e240a43
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_70_2020.tif
  format: null
  id: resource_70a982e4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_65_2020.tif
  format: null
  id: resource_8ca26bc2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_60_2020.tif
  format: null
  id: resource_7c51fca9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_5_2020.tif
  format: null
  id: resource_612f0a93
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_55_2020.tif
  format: null
  id: resource_12141980
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_50_2020.tif
  format: null
  id: resource_ae4c24e6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_45_2020.tif
  format: null
  id: resource_d2adc217
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_40_2020.tif
  format: null
  id: resource_c575ce48
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_35_2020.tif
  format: null
  id: resource_e66a0dc4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_30_2020.tif
  format: null
  id: resource_1d9afac7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_25_2020.tif
  format: null
  id: resource_3bab9dee
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_20_2020.tif
  format: null
  id: resource_26fea288
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_1_2020.tif
  format: null
  id: resource_f2b6e5e3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_15_2020.tif
  format: null
  id: resource_27676cc6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_10_2020.tif
  format: null
  id: resource_813b73de
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_m_0_2020.tif
  format: null
  id: resource_4fe8d4d2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_80_2020.tif
  format: null
  id: resource_465e484c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_75_2020.tif
  format: null
  id: resource_e6d4d182
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_70_2020.tif
  format: null
  id: resource_b4f00015
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_65_2020.tif
  format: null
  id: resource_3332f3d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_60_2020.tif
  format: null
  id: resource_7f0e9dd3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_5_2020.tif
  format: null
  id: resource_76658108
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_55_2020.tif
  format: null
  id: resource_c99f4916
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_50_2020.tif
  format: null
  id: resource_ae3afd5c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_45_2020.tif
  format: null
  id: resource_f0af0d99
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_40_2020.tif
  format: null
  id: resource_a8017bb5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_35_2020.tif
  format: null
  id: resource_8446e643
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_30_2020.tif
  format: null
  id: resource_65626bad
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_25_2020.tif
  format: null
  id: resource_db2a118c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_20_2020.tif
  format: null
  id: resource_6058db3c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_1_2020.tif
  format: null
  id: resource_6d3eda6c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_15_2020.tif
  format: null
  id: resource_675d6681
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_10_2020.tif
  format: null
  id: resource_a6bb77b4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/NIU/niu_f_0_2020.tif
  format: null
  id: resource_57658c22
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_80_2019.tif
  format: null
  id: resource_ba477096
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_75_2019.tif
  format: null
  id: resource_b17943cf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_70_2019.tif
  format: null
  id: resource_26b3fee6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_65_2019.tif
  format: null
  id: resource_cd224b3f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_60_2019.tif
  format: null
  id: resource_c9ebbd4e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_5_2019.tif
  format: null
  id: resource_53066617
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_55_2019.tif
  format: null
  id: resource_a2716511
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_50_2019.tif
  format: null
  id: resource_a856fae4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_45_2019.tif
  format: null
  id: resource_4f3a4699
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_40_2019.tif
  format: null
  id: resource_a78d472e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_35_2019.tif
  format: null
  id: resource_6761563d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_30_2019.tif
  format: null
  id: resource_d4e770ce
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_25_2019.tif
  format: null
  id: resource_0a97a555
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_20_2019.tif
  format: null
  id: resource_a0a514d9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_1_2019.tif
  format: null
  id: resource_d6acdd61
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_15_2019.tif
  format: null
  id: resource_f2d78ad9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_10_2019.tif
  format: null
  id: resource_ad1799bc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_m_0_2019.tif
  format: null
  id: resource_145fef3f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_80_2019.tif
  format: null
  id: resource_80a330e6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_75_2019.tif
  format: null
  id: resource_bf315c76
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_70_2019.tif
  format: null
  id: resource_4c6bea00
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_65_2019.tif
  format: null
  id: resource_45369c3f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_60_2019.tif
  format: null
  id: resource_8d094601
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_5_2019.tif
  format: null
  id: resource_726b2719
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_55_2019.tif
  format: null
  id: resource_94bfbbee
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_50_2019.tif
  format: null
  id: resource_c5b8e10d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_45_2019.tif
  format: null
  id: resource_f1a05b62
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_40_2019.tif
  format: null
  id: resource_63ba7a27
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_35_2019.tif
  format: null
  id: resource_201e65d4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_30_2019.tif
  format: null
  id: resource_eb5b7857
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_25_2019.tif
  format: null
  id: resource_24502c00
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_20_2019.tif
  format: null
  id: resource_60736420
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_1_2019.tif
  format: null
  id: resource_3c28df4b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_15_2019.tif
  format: null
  id: resource_6e6fdf88
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_10_2019.tif
  format: null
  id: resource_34df7269
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/NIU/niu_f_0_2019.tif
  format: null
  id: resource_cf8480ab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_80_2018.tif
  format: null
  id: resource_bc394391
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_75_2018.tif
  format: null
  id: resource_91fe4774
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_70_2018.tif
  format: null
  id: resource_f3131ffb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_65_2018.tif
  format: null
  id: resource_b6e077cb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_60_2018.tif
  format: null
  id: resource_90ac7ef7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_5_2018.tif
  format: null
  id: resource_ec711833
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_55_2018.tif
  format: null
  id: resource_5b343354
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_50_2018.tif
  format: null
  id: resource_b4f97f1c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_45_2018.tif
  format: null
  id: resource_fbaa792a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_40_2018.tif
  format: null
  id: resource_6bcc553b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_35_2018.tif
  format: null
  id: resource_75dd5ba0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_30_2018.tif
  format: null
  id: resource_aee03cd8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_25_2018.tif
  format: null
  id: resource_a3a81c03
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_20_2018.tif
  format: null
  id: resource_f28bb50b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_1_2018.tif
  format: null
  id: resource_dff9a73c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_15_2018.tif
  format: null
  id: resource_06eed201
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_10_2018.tif
  format: null
  id: resource_cfc41d24
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_m_0_2018.tif
  format: null
  id: resource_42bf313b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_80_2018.tif
  format: null
  id: resource_fd3fe2b2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_75_2018.tif
  format: null
  id: resource_4dd99359
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_70_2018.tif
  format: null
  id: resource_e2cdff59
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_65_2018.tif
  format: null
  id: resource_3131fd3f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_60_2018.tif
  format: null
  id: resource_e13e4c50
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_5_2018.tif
  format: null
  id: resource_fc1224e4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_55_2018.tif
  format: null
  id: resource_30302aba
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_50_2018.tif
  format: null
  id: resource_9ca09d25
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_45_2018.tif
  format: null
  id: resource_a826c884
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_40_2018.tif
  format: null
  id: resource_eddfff30
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_35_2018.tif
  format: null
  id: resource_3f989938
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_30_2018.tif
  format: null
  id: resource_c476b7a9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_25_2018.tif
  format: null
  id: resource_1c74e4ad
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_20_2018.tif
  format: null
  id: resource_26732526
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_1_2018.tif
  format: null
  id: resource_d80bab20
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_15_2018.tif
  format: null
  id: resource_dae45a50
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_10_2018.tif
  format: null
  id: resource_9eaf2be0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/NIU/niu_f_0_2018.tif
  format: null
  id: resource_df6266dc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_80_2017.tif
  format: null
  id: resource_363b8755
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_75_2017.tif
  format: null
  id: resource_1c81b6d2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_70_2017.tif
  format: null
  id: resource_dfe79698
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_65_2017.tif
  format: null
  id: resource_de004c91
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_60_2017.tif
  format: null
  id: resource_dcca19bb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_5_2017.tif
  format: null
  id: resource_d573c6f3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_55_2017.tif
  format: null
  id: resource_59b87f01
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_50_2017.tif
  format: null
  id: resource_0ae707bd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_45_2017.tif
  format: null
  id: resource_9260617d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_40_2017.tif
  format: null
  id: resource_cc56e0ec
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_35_2017.tif
  format: null
  id: resource_87e4d87f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_30_2017.tif
  format: null
  id: resource_3efbce86
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_25_2017.tif
  format: null
  id: resource_970ed5da
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_20_2017.tif
  format: null
  id: resource_023f1d4e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_1_2017.tif
  format: null
  id: resource_63f3c0a4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_15_2017.tif
  format: null
  id: resource_11d9c3f9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_10_2017.tif
  format: null
  id: resource_3e330558
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_m_0_2017.tif
  format: null
  id: resource_ef29c569
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_80_2017.tif
  format: null
  id: resource_b56b9f1a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_75_2017.tif
  format: null
  id: resource_5edcb00f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_70_2017.tif
  format: null
  id: resource_ad971c9a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_65_2017.tif
  format: null
  id: resource_a64310f7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_60_2017.tif
  format: null
  id: resource_8c807842
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_5_2017.tif
  format: null
  id: resource_b0008f16
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_55_2017.tif
  format: null
  id: resource_a04babec
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_50_2017.tif
  format: null
  id: resource_a4ce99f2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_45_2017.tif
  format: null
  id: resource_b3da8ca2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_40_2017.tif
  format: null
  id: resource_23bcc819
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_35_2017.tif
  format: null
  id: resource_c13fe55d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_30_2017.tif
  format: null
  id: resource_69f641e0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_25_2017.tif
  format: null
  id: resource_ab66545a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_20_2017.tif
  format: null
  id: resource_7ef9f092
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_1_2017.tif
  format: null
  id: resource_ed124cd2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_15_2017.tif
  format: null
  id: resource_8342d09e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_10_2017.tif
  format: null
  id: resource_64e95632
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/NIU/niu_f_0_2017.tif
  format: null
  id: resource_3ff219f4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_80_2016.tif
  format: null
  id: resource_0ef3621d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_75_2016.tif
  format: null
  id: resource_3b782067
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_70_2016.tif
  format: null
  id: resource_65879433
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_65_2016.tif
  format: null
  id: resource_3d35e0c7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_60_2016.tif
  format: null
  id: resource_e931c543
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_5_2016.tif
  format: null
  id: resource_739999f4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_55_2016.tif
  format: null
  id: resource_b4c055cc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_50_2016.tif
  format: null
  id: resource_818d178b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_45_2016.tif
  format: null
  id: resource_1b20cd73
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_40_2016.tif
  format: null
  id: resource_f3e98ca1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_35_2016.tif
  format: null
  id: resource_ce8d0d62
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_30_2016.tif
  format: null
  id: resource_1bc0f834
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_25_2016.tif
  format: null
  id: resource_ed072c8a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_20_2016.tif
  format: null
  id: resource_896c9728
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_1_2016.tif
  format: null
  id: resource_ddeea519
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_15_2016.tif
  format: null
  id: resource_b1a707a5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_10_2016.tif
  format: null
  id: resource_6485afaa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_m_0_2016.tif
  format: null
  id: resource_90da388b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_m_0_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_80_2016.tif
  format: null
  id: resource_b1eb90b0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_75_2016.tif
  format: null
  id: resource_e7c425b1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_70_2016.tif
  format: null
  id: resource_cf545ab4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_65_2016.tif
  format: null
  id: resource_e60e38e2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_60_2016.tif
  format: null
  id: resource_a0b328fc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_5_2016.tif
  format: null
  id: resource_9977de45
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_55_2016.tif
  format: null
  id: resource_705c1572
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_50_2016.tif
  format: null
  id: resource_3fca7b2a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_45_2016.tif
  format: null
  id: resource_82b16a65
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_40_2016.tif
  format: null
  id: resource_a07cbd1d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_35_2016.tif
  format: null
  id: resource_07548804
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_30_2016.tif
  format: null
  id: resource_66dfff4e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_25_2016.tif
  format: null
  id: resource_3630a654
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_20_2016.tif
  format: null
  id: resource_18fad782
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_1_2016.tif
  format: null
  id: resource_0f970f54
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_15_2016.tif
  format: null
  id: resource_45d89a69
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_10_2016.tif
  format: null
  id: resource_c2eb51f1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Niue - Age and gender structures (Niue 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/NIU/niu_f_0_2016.tif
  format: null
  id: resource_0cf5b61f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: niu_f_0_2016.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-niu_worldpop_niueagegenderstructures_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - NIU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Niue - Age and gender structures
version: null
vulnerability: null
---
