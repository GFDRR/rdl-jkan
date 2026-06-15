---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-pitcairn
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-pitcairn
dataset_id: rdls_exp-pcn_worldpop_pitcairnagegenderstructur_2000
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
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-pitcairn]'
details: null
exposure:
- asset_type:
    description: Gridded population counts disaggregated by gender and age groups
      (0-14, 15-64, 65+) at 100m resolution for 2017-2020
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
  description: WorldPop applied spatial disaggregation modeling methods (Tatem et
    al., Pezzulo et al.) to census and survey population data to produce gridded population
    counts stratified by gender and age group at 100m resolution. The dataset provides
    annual estimates for Pitcairn Islands from 2017-2020 in GeoTIFF format.
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-pitcairn
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
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/PCN/pcn_m_65_2020.tif
  format: null
  id: resource_5276e88e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/PCN/pcn_m_15_2020.tif
  format: null
  id: resource_ae262f93
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/PCN/pcn_m_0_2020.tif
  format: null
  id: resource_d0f86ce9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/PCN/pcn_f_65_2020.tif
  format: null
  id: resource_f3749a8f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/PCN/pcn_f_15_2020.tif
  format: null
  id: resource_7f3c3ff5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/PCN/pcn_f_0_2020.tif
  format: null
  id: resource_ced5c736
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/PCN/pcn_m_65_2019.tif
  format: null
  id: resource_72424192
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/PCN/pcn_m_15_2019.tif
  format: null
  id: resource_082aac7a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/PCN/pcn_m_0_2019.tif
  format: null
  id: resource_0733ba13
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/PCN/pcn_f_65_2019.tif
  format: null
  id: resource_4f7b154d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/PCN/pcn_f_15_2019.tif
  format: null
  id: resource_5b720a70
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/PCN/pcn_f_0_2019.tif
  format: null
  id: resource_4fb0e9bf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/PCN/pcn_m_65_2018.tif
  format: null
  id: resource_cb827f47
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/PCN/pcn_m_15_2018.tif
  format: null
  id: resource_26b25a65
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/PCN/pcn_m_0_2018.tif
  format: null
  id: resource_2e224e6c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/PCN/pcn_f_65_2018.tif
  format: null
  id: resource_9fd9a87c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/PCN/pcn_f_15_2018.tif
  format: null
  id: resource_2dec1c07
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/PCN/pcn_f_0_2018.tif
  format: null
  id: resource_4bbbdbb9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_m_65_2017.tif
  format: null
  id: resource_9f61a068
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_m_15_2017.tif
  format: null
  id: resource_c2969dc2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_m_0_2017.tif
  format: null
  id: resource_ebf65b39
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_65_2017.tif
  format: null
  id: resource_5748613d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_5_2017.tif
  format: null
  id: resource_e4d39974
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_55_2017.tif
  format: null
  id: resource_d712c23c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_50_2017.tif
  format: null
  id: resource_50443fd0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_45_2017.tif
  format: null
  id: resource_aff7f6f9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_40_2017.tif
  format: null
  id: resource_358cfbbc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_35_2017.tif
  format: null
  id: resource_25844246
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_30_2017.tif
  format: null
  id: resource_2aad732a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_25_2017.tif
  format: null
  id: resource_623862e5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_20_2017.tif
  format: null
  id: resource_fb4633c5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_1_2017.tif
  format: null
  id: resource_6300a8d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_15_2017.tif
  format: null
  id: resource_0265be32
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_10_2017.tif
  format: null
  id: resource_79c9abc0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/PCN/pcn_f_0_2017.tif
  format: null
  id: resource_fcfa0d6f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_80_2016.tif
  format: null
  id: resource_e6eaf255
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_75_2016.tif
  format: null
  id: resource_f64059c3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_70_2016.tif
  format: null
  id: resource_603309b4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_65_2016.tif
  format: null
  id: resource_aea12805
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_60_2016.tif
  format: null
  id: resource_e87579c7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_5_2016.tif
  format: null
  id: resource_81fde025
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_55_2016.tif
  format: null
  id: resource_dcabc515
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_50_2016.tif
  format: null
  id: resource_2400fd45
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_45_2016.tif
  format: null
  id: resource_c3d183a0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_40_2016.tif
  format: null
  id: resource_0210ab12
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_35_2016.tif
  format: null
  id: resource_c9e1d9bb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_30_2016.tif
  format: null
  id: resource_e34145d3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_25_2016.tif
  format: null
  id: resource_a5dab427
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_20_2016.tif
  format: null
  id: resource_7b4623a5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_1_2016.tif
  format: null
  id: resource_a6960a26
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_15_2016.tif
  format: null
  id: resource_a242e07c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_10_2016.tif
  format: null
  id: resource_38229623
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_m_0_2016.tif
  format: null
  id: resource_9bc70013
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_m_0_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_80_2016.tif
  format: null
  id: resource_788b42f5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_75_2016.tif
  format: null
  id: resource_5238e412
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_70_2016.tif
  format: null
  id: resource_c7a09cc2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_65_2016.tif
  format: null
  id: resource_2e5d2393
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_60_2016.tif
  format: null
  id: resource_c404b773
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_5_2016.tif
  format: null
  id: resource_c731b68c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_55_2016.tif
  format: null
  id: resource_96c0fea0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_50_2016.tif
  format: null
  id: resource_e96fa4cb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_45_2016.tif
  format: null
  id: resource_e48c0b98
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_40_2016.tif
  format: null
  id: resource_37b18d7e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_35_2016.tif
  format: null
  id: resource_1157eeae
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_30_2016.tif
  format: null
  id: resource_6e241271
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_25_2016.tif
  format: null
  id: resource_62a56525
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_20_2016.tif
  format: null
  id: resource_461fb2cf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_1_2016.tif
  format: null
  id: resource_a5940987
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_15_2016.tif
  format: null
  id: resource_9af711f2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_10_2016.tif
  format: null
  id: resource_de99848d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Pitcairn - Age and gender structures (Pitcairn Islands 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/PCN/pcn_f_0_2016.tif
  format: null
  id: resource_8f334622
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: pcn_f_0_2016.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-pcn_worldpop_pitcairnagegenderstructur_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - PCN
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Pitcairn - Age and gender structures
version: null
vulnerability: null
---
