---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-reunion
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-reunion
dataset_id: rdls_exp-reu_worldpop_reunionagegenderstructure_2000
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
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-reunion]'
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
  description: "WorldPop applied spatial disaggregation methods to census and survey\
    \ population data to produce age and gender-structured gridded population counts\
    \ at 3 arc-second resolution (~100m) for R\xE9union in 2020. The dataset comprises\
    \ separate GeoTIFF rasters for each age group and gender category, enabling disaster\
    \ risk exposure assessment by demographic structure."
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-reunion
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
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_80_2020.tif
  format: null
  id: resource_bf7c0e9d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_75_2020.tif
  format: null
  id: resource_983b89d0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_70_2020.tif
  format: null
  id: resource_6b207ca4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_65_2020.tif
  format: null
  id: resource_eb3bd740
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_60_2020.tif
  format: null
  id: resource_f030c293
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_5_2020.tif
  format: null
  id: resource_bc2ecb9a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_55_2020.tif
  format: null
  id: resource_7579684a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_50_2020.tif
  format: null
  id: resource_ccee6fdb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_45_2020.tif
  format: null
  id: resource_ba77f368
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_40_2020.tif
  format: null
  id: resource_575e8501
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_35_2020.tif
  format: null
  id: resource_aa5b9486
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_30_2020.tif
  format: null
  id: resource_49749eb6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_25_2020.tif
  format: null
  id: resource_489dbf13
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_20_2020.tif
  format: null
  id: resource_2395026a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_1_2020.tif
  format: null
  id: resource_05271084
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_15_2020.tif
  format: null
  id: resource_a4da038f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_10_2020.tif
  format: null
  id: resource_e14f4193
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_m_0_2020.tif
  format: null
  id: resource_e3eb8adf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_80_2020.tif
  format: null
  id: resource_f0e0fa54
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_75_2020.tif
  format: null
  id: resource_3ef35f65
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_70_2020.tif
  format: null
  id: resource_fc236c57
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_65_2020.tif
  format: null
  id: resource_0c6293ed
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_60_2020.tif
  format: null
  id: resource_ad77d0ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_5_2020.tif
  format: null
  id: resource_d8df5066
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_55_2020.tif
  format: null
  id: resource_f4e60cac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_50_2020.tif
  format: null
  id: resource_c296387b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_45_2020.tif
  format: null
  id: resource_4e8fd176
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_40_2020.tif
  format: null
  id: resource_3474759d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_35_2020.tif
  format: null
  id: resource_ec911369
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_30_2020.tif
  format: null
  id: resource_b2ea07ea
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_25_2020.tif
  format: null
  id: resource_8389d02d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_20_2020.tif
  format: null
  id: resource_e0629892
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_1_2020.tif
  format: null
  id: resource_5a1d3665
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_15_2020.tif
  format: null
  id: resource_cd3c7f62
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_10_2020.tif
  format: null
  id: resource_6b8b5e5a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/REU/reu_f_0_2020.tif
  format: null
  id: resource_3b221252
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_80_2019.tif
  format: null
  id: resource_b111d20e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_75_2019.tif
  format: null
  id: resource_f1acc6f9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_70_2019.tif
  format: null
  id: resource_cf6fb676
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_65_2019.tif
  format: null
  id: resource_f52a2199
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_60_2019.tif
  format: null
  id: resource_cdb658e6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_5_2019.tif
  format: null
  id: resource_a6db9daa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_55_2019.tif
  format: null
  id: resource_c4ada1ba
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_50_2019.tif
  format: null
  id: resource_092f4c10
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_45_2019.tif
  format: null
  id: resource_ee3a71d3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_40_2019.tif
  format: null
  id: resource_026b5785
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_35_2019.tif
  format: null
  id: resource_6a0a814c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_30_2019.tif
  format: null
  id: resource_827ae126
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_25_2019.tif
  format: null
  id: resource_d0759d61
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_20_2019.tif
  format: null
  id: resource_ab2f1a59
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_1_2019.tif
  format: null
  id: resource_464652a1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_15_2019.tif
  format: null
  id: resource_7a441d85
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_10_2019.tif
  format: null
  id: resource_7f9e3802
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_m_0_2019.tif
  format: null
  id: resource_729651d4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_80_2019.tif
  format: null
  id: resource_6971228d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_75_2019.tif
  format: null
  id: resource_649d2590
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_70_2019.tif
  format: null
  id: resource_50f02504
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_65_2019.tif
  format: null
  id: resource_a5647673
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_60_2019.tif
  format: null
  id: resource_386d1286
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_5_2019.tif
  format: null
  id: resource_ae7fdef7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_55_2019.tif
  format: null
  id: resource_cb4c8ff8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_50_2019.tif
  format: null
  id: resource_afea1482
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_45_2019.tif
  format: null
  id: resource_2c856678
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_40_2019.tif
  format: null
  id: resource_95416a92
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_35_2019.tif
  format: null
  id: resource_b0c1aafc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_30_2019.tif
  format: null
  id: resource_95b52c06
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_25_2019.tif
  format: null
  id: resource_4eb86951
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_20_2019.tif
  format: null
  id: resource_5ecc134d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_1_2019.tif
  format: null
  id: resource_d8cb5227
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_15_2019.tif
  format: null
  id: resource_23089340
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_10_2019.tif
  format: null
  id: resource_122b3045
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/REU/reu_f_0_2019.tif
  format: null
  id: resource_e8969e53
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_80_2018.tif
  format: null
  id: resource_34dc08d9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_75_2018.tif
  format: null
  id: resource_3cc488df
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_70_2018.tif
  format: null
  id: resource_ad90c15c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_65_2018.tif
  format: null
  id: resource_6327da04
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_60_2018.tif
  format: null
  id: resource_17682883
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_5_2018.tif
  format: null
  id: resource_c36c25c7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_55_2018.tif
  format: null
  id: resource_67a23b08
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_50_2018.tif
  format: null
  id: resource_3c7cf16b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_45_2018.tif
  format: null
  id: resource_9d980e68
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_40_2018.tif
  format: null
  id: resource_524b2201
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_35_2018.tif
  format: null
  id: resource_f9abed50
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_30_2018.tif
  format: null
  id: resource_d255bbba
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_25_2018.tif
  format: null
  id: resource_ff32ba87
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_20_2018.tif
  format: null
  id: resource_ca277737
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_1_2018.tif
  format: null
  id: resource_8bd344ab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_15_2018.tif
  format: null
  id: resource_075bc748
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_10_2018.tif
  format: null
  id: resource_eb026464
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_m_0_2018.tif
  format: null
  id: resource_082674f4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_80_2018.tif
  format: null
  id: resource_b90f561e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_75_2018.tif
  format: null
  id: resource_3d7de9e4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_70_2018.tif
  format: null
  id: resource_d289ae9b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_65_2018.tif
  format: null
  id: resource_ec2544c0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_60_2018.tif
  format: null
  id: resource_95dee7df
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_5_2018.tif
  format: null
  id: resource_7831c715
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_55_2018.tif
  format: null
  id: resource_ebd9de84
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_50_2018.tif
  format: null
  id: resource_c4f4b3e7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_45_2018.tif
  format: null
  id: resource_cd57ec76
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_40_2018.tif
  format: null
  id: resource_91a41f92
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_35_2018.tif
  format: null
  id: resource_b610d204
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_30_2018.tif
  format: null
  id: resource_5d85915e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_25_2018.tif
  format: null
  id: resource_65cce0fa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_20_2018.tif
  format: null
  id: resource_f5dc437d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_1_2018.tif
  format: null
  id: resource_c9cfc634
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_15_2018.tif
  format: null
  id: resource_4a9f6bc8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_10_2018.tif
  format: null
  id: resource_ff760276
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/REU/reu_f_0_2018.tif
  format: null
  id: resource_c61e231c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_80_2017.tif
  format: null
  id: resource_c91ebee4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_75_2017.tif
  format: null
  id: resource_0ea70a30
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_70_2017.tif
  format: null
  id: resource_f90d132a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_65_2017.tif
  format: null
  id: resource_470955be
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_60_2017.tif
  format: null
  id: resource_c86c2710
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_5_2017.tif
  format: null
  id: resource_da7ac48f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_55_2017.tif
  format: null
  id: resource_d63f0425
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_50_2017.tif
  format: null
  id: resource_e5308e29
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_45_2017.tif
  format: null
  id: resource_bce2bdc6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_40_2017.tif
  format: null
  id: resource_241e88af
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_35_2017.tif
  format: null
  id: resource_68998e75
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_30_2017.tif
  format: null
  id: resource_1f9ab23f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_25_2017.tif
  format: null
  id: resource_753a67ad
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_20_2017.tif
  format: null
  id: resource_398f25dc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_1_2017.tif
  format: null
  id: resource_ca707cd9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_15_2017.tif
  format: null
  id: resource_da791c02
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_10_2017.tif
  format: null
  id: resource_44c7fb9c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_m_0_2017.tif
  format: null
  id: resource_85686dc9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_80_2017.tif
  format: null
  id: resource_e1cacc97
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_75_2017.tif
  format: null
  id: resource_db7530d5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_70_2017.tif
  format: null
  id: resource_4302105a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_65_2017.tif
  format: null
  id: resource_e4856073
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_60_2017.tif
  format: null
  id: resource_e36a4746
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_5_2017.tif
  format: null
  id: resource_b0261822
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_55_2017.tif
  format: null
  id: resource_19e3388d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_50_2017.tif
  format: null
  id: resource_6645bb74
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_45_2017.tif
  format: null
  id: resource_b7eeeb66
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_40_2017.tif
  format: null
  id: resource_73d4facb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_35_2017.tif
  format: null
  id: resource_87603202
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_30_2017.tif
  format: null
  id: resource_38a2b872
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_25_2017.tif
  format: null
  id: resource_9c0a51f0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_20_2017.tif
  format: null
  id: resource_191ace3d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_1_2017.tif
  format: null
  id: resource_6a5ca4ba
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_15_2017.tif
  format: null
  id: resource_5820d3e4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_10_2017.tif
  format: null
  id: resource_505de3fe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/REU/reu_f_0_2017.tif
  format: null
  id: resource_2961f784
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_80_2016.tif
  format: null
  id: resource_f6958f06
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_75_2016.tif
  format: null
  id: resource_db46c5f4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_70_2016.tif
  format: null
  id: resource_a651f53b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_65_2016.tif
  format: null
  id: resource_2ce5304f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_60_2016.tif
  format: null
  id: resource_2d2dc6a9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_5_2016.tif
  format: null
  id: resource_99bd4975
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_55_2016.tif
  format: null
  id: resource_4f1a1e67
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_50_2016.tif
  format: null
  id: resource_4f42289d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_45_2016.tif
  format: null
  id: resource_9eeb8107
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_40_2016.tif
  format: null
  id: resource_e06b49d5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_35_2016.tif
  format: null
  id: resource_a67d9c86
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_30_2016.tif
  format: null
  id: resource_a28238ef
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_25_2016.tif
  format: null
  id: resource_a9f10dd4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_20_2016.tif
  format: null
  id: resource_48f727f0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_1_2016.tif
  format: null
  id: resource_16a8acfa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_15_2016.tif
  format: null
  id: resource_1fa317f5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_10_2016.tif
  format: null
  id: resource_279244be
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_m_0_2016.tif
  format: null
  id: resource_af3a8585
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_m_0_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_80_2016.tif
  format: null
  id: resource_508db414
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_75_2016.tif
  format: null
  id: resource_cc647871
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_70_2016.tif
  format: null
  id: resource_aa771c77
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_65_2016.tif
  format: null
  id: resource_0c298f13
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_60_2016.tif
  format: null
  id: resource_0718c8e4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_5_2016.tif
  format: null
  id: resource_60e9ac8c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_55_2016.tif
  format: null
  id: resource_017d4762
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_50_2016.tif
  format: null
  id: resource_165f66ae
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_45_2016.tif
  format: null
  id: resource_5369ec27
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_40_2016.tif
  format: null
  id: resource_1b95e025
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_35_2016.tif
  format: null
  id: resource_4b815e82
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_30_2016.tif
  format: null
  id: resource_48f68a9a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_25_2016.tif
  format: null
  id: resource_2a48e02e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_20_2016.tif
  format: null
  id: resource_6552241a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_1_2016.tif
  format: null
  id: resource_3e60ccce
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_15_2016.tif
  format: null
  id: resource_9da9d714
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_10_2016.tif
  format: null
  id: resource_c12e39c8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "R\xE9union - Age and gender structures (R\xE9union 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/REU/reu_f_0_2016.tif
  format: null
  id: resource_61da9b69
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: reu_f_0_2016.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-reu_worldpop_reunionagegenderstructure_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - REU
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: "R\xE9union - Age and gender structures"
version: null
vulnerability: null
---
