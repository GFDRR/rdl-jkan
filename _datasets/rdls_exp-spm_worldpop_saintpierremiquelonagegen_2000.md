---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-saint-pierre-and-miquelon
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-saint-pierre-and-miquelon
dataset_id: rdls_exp-spm_worldpop_saintpierremiquelonagegen_2000
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
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-saint-pierre-and-miquelon]'
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
  description: WorldPop generated gridded population estimates by disaggregating baseline
    population counts by age group and gender using demographic modeling methods (Tatem
    et al., Pezzulo et al.). The resulting dataset provides raster layers at 3 arc-second
    resolution (~100m) for each age-gender cohort in Saint Pierre and Miquelon for
    2020.
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-saint-pierre-and-miquelon
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
referenced_by: []
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_80_2020.tif
  format: null
  id: resource_f1af4542
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_75_2020.tif
  format: null
  id: resource_c8ba5a44
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_70_2020.tif
  format: null
  id: resource_266d1273
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_65_2020.tif
  format: null
  id: resource_cec91a81
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_60_2020.tif
  format: null
  id: resource_bbe4203a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_5_2020.tif
  format: null
  id: resource_19984901
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_55_2020.tif
  format: null
  id: resource_72284fa1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_50_2020.tif
  format: null
  id: resource_be315f31
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_45_2020.tif
  format: null
  id: resource_0268a123
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_40_2020.tif
  format: null
  id: resource_efe95cd0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_35_2020.tif
  format: null
  id: resource_8f757d20
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_30_2020.tif
  format: null
  id: resource_f15565d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_25_2020.tif
  format: null
  id: resource_6c0d1d8d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_20_2020.tif
  format: null
  id: resource_ef39e214
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_1_2020.tif
  format: null
  id: resource_50517eef
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_15_2020.tif
  format: null
  id: resource_8c7dbc83
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_10_2020.tif
  format: null
  id: resource_e156dcc1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_m_0_2020.tif
  format: null
  id: resource_c44f9fe2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_80_2020.tif
  format: null
  id: resource_d96b7767
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_75_2020.tif
  format: null
  id: resource_567ffffe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_70_2020.tif
  format: null
  id: resource_f5db9794
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_65_2020.tif
  format: null
  id: resource_e4154cf5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_60_2020.tif
  format: null
  id: resource_bfa1e221
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_5_2020.tif
  format: null
  id: resource_25eda4d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_55_2020.tif
  format: null
  id: resource_269df2f0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_50_2020.tif
  format: null
  id: resource_0d688c8c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_45_2020.tif
  format: null
  id: resource_5a9eb6c6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_40_2020.tif
  format: null
  id: resource_0f1722e9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_35_2020.tif
  format: null
  id: resource_b97684fb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_30_2020.tif
  format: null
  id: resource_ee885215
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_25_2020.tif
  format: null
  id: resource_17d5b7a0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_20_2020.tif
  format: null
  id: resource_ce9ecfd9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_1_2020.tif
  format: null
  id: resource_435da955
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_15_2020.tif
  format: null
  id: resource_1a149eb9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_10_2020.tif
  format: null
  id: resource_dc92687d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/SPM/spm_f_0_2020.tif
  format: null
  id: resource_0bf38fe6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_80_2019.tif
  format: null
  id: resource_5ada0dc5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_75_2019.tif
  format: null
  id: resource_d336e346
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_70_2019.tif
  format: null
  id: resource_e00a5222
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_65_2019.tif
  format: null
  id: resource_b669cd64
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_60_2019.tif
  format: null
  id: resource_4cc80862
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_5_2019.tif
  format: null
  id: resource_c0079c68
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_55_2019.tif
  format: null
  id: resource_d8a1ccbb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_50_2019.tif
  format: null
  id: resource_3cb7d608
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_45_2019.tif
  format: null
  id: resource_b90567ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_40_2019.tif
  format: null
  id: resource_cd4d3335
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_35_2019.tif
  format: null
  id: resource_493539a8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_30_2019.tif
  format: null
  id: resource_001af8cd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_25_2019.tif
  format: null
  id: resource_649adde2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_20_2019.tif
  format: null
  id: resource_f4ff5b77
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_1_2019.tif
  format: null
  id: resource_f36245fc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_15_2019.tif
  format: null
  id: resource_d0ec6e06
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_10_2019.tif
  format: null
  id: resource_36fc6333
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_m_0_2019.tif
  format: null
  id: resource_99326edd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_80_2019.tif
  format: null
  id: resource_4a9703b6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_75_2019.tif
  format: null
  id: resource_41c19823
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_70_2019.tif
  format: null
  id: resource_ec1503b7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_65_2019.tif
  format: null
  id: resource_1bc519ab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_60_2019.tif
  format: null
  id: resource_c1919244
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_5_2019.tif
  format: null
  id: resource_bd28bb9b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_55_2019.tif
  format: null
  id: resource_71cdea3f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_50_2019.tif
  format: null
  id: resource_46416de3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_45_2019.tif
  format: null
  id: resource_d5763d70
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_40_2019.tif
  format: null
  id: resource_b79fb689
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_35_2019.tif
  format: null
  id: resource_2f1bded7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_30_2019.tif
  format: null
  id: resource_aee55811
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_25_2019.tif
  format: null
  id: resource_a510fdf8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_20_2019.tif
  format: null
  id: resource_0155d83b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_1_2019.tif
  format: null
  id: resource_5a645b56
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_15_2019.tif
  format: null
  id: resource_0c531ce9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_10_2019.tif
  format: null
  id: resource_9d0141b9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/SPM/spm_f_0_2019.tif
  format: null
  id: resource_2f20f529
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_80_2018.tif
  format: null
  id: resource_19f4ec45
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_75_2018.tif
  format: null
  id: resource_11efd80c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_70_2018.tif
  format: null
  id: resource_0a849362
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_65_2018.tif
  format: null
  id: resource_aa9d5fb3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_60_2018.tif
  format: null
  id: resource_34c7af66
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_5_2018.tif
  format: null
  id: resource_deb04e4f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_55_2018.tif
  format: null
  id: resource_4e3446b9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_50_2018.tif
  format: null
  id: resource_f6c50ebb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_45_2018.tif
  format: null
  id: resource_aab6b014
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_40_2018.tif
  format: null
  id: resource_dabdeb3b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_35_2018.tif
  format: null
  id: resource_a67b2071
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_30_2018.tif
  format: null
  id: resource_20ad1476
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_25_2018.tif
  format: null
  id: resource_c6889220
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_20_2018.tif
  format: null
  id: resource_be96bed1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_1_2018.tif
  format: null
  id: resource_cd5096b5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_15_2018.tif
  format: null
  id: resource_2b3e98ab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_10_2018.tif
  format: null
  id: resource_48d7756a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_m_0_2018.tif
  format: null
  id: resource_a1df617c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_80_2018.tif
  format: null
  id: resource_474312ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_75_2018.tif
  format: null
  id: resource_41f299af
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_70_2018.tif
  format: null
  id: resource_2c9e8ea6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_65_2018.tif
  format: null
  id: resource_60e1b7cb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_60_2018.tif
  format: null
  id: resource_fecaf09a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_5_2018.tif
  format: null
  id: resource_1e40c5a9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_55_2018.tif
  format: null
  id: resource_d1e14a2a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_50_2018.tif
  format: null
  id: resource_0e23839f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_45_2018.tif
  format: null
  id: resource_27a87089
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_40_2018.tif
  format: null
  id: resource_03a86e08
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_35_2018.tif
  format: null
  id: resource_912b9bdc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_30_2018.tif
  format: null
  id: resource_45191ffd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_25_2018.tif
  format: null
  id: resource_f0fac9fa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_20_2018.tif
  format: null
  id: resource_bbd988dd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_1_2018.tif
  format: null
  id: resource_63287904
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_15_2018.tif
  format: null
  id: resource_faba9d42
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_10_2018.tif
  format: null
  id: resource_b9deba60
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/SPM/spm_f_0_2018.tif
  format: null
  id: resource_f9d0175b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_80_2017.tif
  format: null
  id: resource_7bcd87ff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_75_2017.tif
  format: null
  id: resource_14449e8e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_70_2017.tif
  format: null
  id: resource_f5db2661
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_65_2017.tif
  format: null
  id: resource_7e2ee31d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_60_2017.tif
  format: null
  id: resource_9042ab77
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_5_2017.tif
  format: null
  id: resource_53eac24c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_55_2017.tif
  format: null
  id: resource_7e17c613
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_50_2017.tif
  format: null
  id: resource_c075be7d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_45_2017.tif
  format: null
  id: resource_5b8e1d98
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_40_2017.tif
  format: null
  id: resource_66978a02
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_35_2017.tif
  format: null
  id: resource_1b69ad35
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_30_2017.tif
  format: null
  id: resource_53b84b3c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_25_2017.tif
  format: null
  id: resource_fd17fb14
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_20_2017.tif
  format: null
  id: resource_a8a79c0b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_1_2017.tif
  format: null
  id: resource_b3fc07dc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_15_2017.tif
  format: null
  id: resource_b5181e01
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_10_2017.tif
  format: null
  id: resource_d07ba867
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_m_0_2017.tif
  format: null
  id: resource_e5282b5a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_80_2017.tif
  format: null
  id: resource_e409169c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_75_2017.tif
  format: null
  id: resource_d07a54ca
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_70_2017.tif
  format: null
  id: resource_ce1d668e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_65_2017.tif
  format: null
  id: resource_813ef965
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_60_2017.tif
  format: null
  id: resource_3b1f7232
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_5_2017.tif
  format: null
  id: resource_d82df036
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_55_2017.tif
  format: null
  id: resource_e0ee7100
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_50_2017.tif
  format: null
  id: resource_e6a0dade
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_45_2017.tif
  format: null
  id: resource_9aa25be4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_40_2017.tif
  format: null
  id: resource_6cca5e0b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_35_2017.tif
  format: null
  id: resource_aec71c17
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_30_2017.tif
  format: null
  id: resource_b73f92a1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_25_2017.tif
  format: null
  id: resource_d3b13961
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_20_2017.tif
  format: null
  id: resource_757a6b89
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_1_2017.tif
  format: null
  id: resource_016aa633
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_15_2017.tif
  format: null
  id: resource_cc1aaee4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_10_2017.tif
  format: null
  id: resource_ae4b6762
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/SPM/spm_f_0_2017.tif
  format: null
  id: resource_bcff8df1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_80_2016.tif
  format: null
  id: resource_62782288
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_75_2016.tif
  format: null
  id: resource_b75ff970
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_70_2016.tif
  format: null
  id: resource_110e5394
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_65_2016.tif
  format: null
  id: resource_3cc8bde1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_60_2016.tif
  format: null
  id: resource_b1ab31ff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_5_2016.tif
  format: null
  id: resource_cde751fa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_55_2016.tif
  format: null
  id: resource_67638194
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_50_2016.tif
  format: null
  id: resource_8df6c192
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_45_2016.tif
  format: null
  id: resource_84d96073
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_40_2016.tif
  format: null
  id: resource_cc8109f9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_35_2016.tif
  format: null
  id: resource_730db694
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_30_2016.tif
  format: null
  id: resource_d7c83e45
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_25_2016.tif
  format: null
  id: resource_c30d390f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_20_2016.tif
  format: null
  id: resource_e59d2b95
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_1_2016.tif
  format: null
  id: resource_42de2aff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_15_2016.tif
  format: null
  id: resource_c1abbacb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_10_2016.tif
  format: null
  id: resource_ff5031df
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_m_0_2016.tif
  format: null
  id: resource_68f95075
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_m_0_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_80_2016.tif
  format: null
  id: resource_fd626d7b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_75_2016.tif
  format: null
  id: resource_a554aa65
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_70_2016.tif
  format: null
  id: resource_a211c5a3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_65_2016.tif
  format: null
  id: resource_26f97704
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_60_2016.tif
  format: null
  id: resource_56c642ba
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_5_2016.tif
  format: null
  id: resource_a8dfe292
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_55_2016.tif
  format: null
  id: resource_2fdc1fc5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_50_2016.tif
  format: null
  id: resource_15d73970
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_45_2016.tif
  format: null
  id: resource_9494c225
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_40_2016.tif
  format: null
  id: resource_b6a950d2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_35_2016.tif
  format: null
  id: resource_6c72f490
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_30_2016.tif
  format: null
  id: resource_6a8be6d8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_25_2016.tif
  format: null
  id: resource_eefbea07
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_20_2016.tif
  format: null
  id: resource_b7f0ace5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_1_2016.tif
  format: null
  id: resource_cbca17e5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_15_2016.tif
  format: null
  id: resource_1c46c81b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_10_2016.tif
  format: null
  id: resource_08c092c1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Saint Pierre and Miquelon 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/SPM/spm_f_0_2016.tif
  format: null
  id: resource_70ddbcb2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: spm_f_0_2016.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-spm_worldpop_saintpierremiquelonagegen_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - SPM
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Saint Pierre and Miquelon - Age and gender structures
version: null
vulnerability: null
---
