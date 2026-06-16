---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-northern-mariana-islands
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-northern-mariana-islands
dataset_id: rdls_exp-mnp_worldpop_northernmarianaislandsage_2000
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
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-northern-mariana-islands]'
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
    et al.) to census and administrative population data to generate age and gender-structured
    population grids at 3 arc-second resolution (~100m) for Northern Mariana Islands
    in 2020. The dataset provides population counts per grid cell stratified by 5-year
    age bands and gender.
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-northern-mariana-islands
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
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_80_2020.tif
  format: null
  id: resource_0f51f3a3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_75_2020.tif
  format: null
  id: resource_e539681e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_70_2020.tif
  format: null
  id: resource_dd3710a5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_65_2020.tif
  format: null
  id: resource_e3d6a5f0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_60_2020.tif
  format: null
  id: resource_cc08c0c0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_5_2020.tif
  format: null
  id: resource_330bfc9e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_55_2020.tif
  format: null
  id: resource_65c3a697
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_50_2020.tif
  format: null
  id: resource_351e01db
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_45_2020.tif
  format: null
  id: resource_86cf6151
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_40_2020.tif
  format: null
  id: resource_479d407a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_35_2020.tif
  format: null
  id: resource_f0c42af8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_30_2020.tif
  format: null
  id: resource_0c60617c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_25_2020.tif
  format: null
  id: resource_d2c35e26
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_20_2020.tif
  format: null
  id: resource_7707fc88
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_1_2020.tif
  format: null
  id: resource_b032654a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_15_2020.tif
  format: null
  id: resource_3b279876
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_10_2020.tif
  format: null
  id: resource_a06d7cd8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_m_0_2020.tif
  format: null
  id: resource_0f661e2d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_80_2020.tif
  format: null
  id: resource_d62cffd1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_75_2020.tif
  format: null
  id: resource_5e7d5bd6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_70_2020.tif
  format: null
  id: resource_b2ac7b50
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_65_2020.tif
  format: null
  id: resource_9a3d67a4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_60_2020.tif
  format: null
  id: resource_fd029f7b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_5_2020.tif
  format: null
  id: resource_15521525
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_55_2020.tif
  format: null
  id: resource_80978a06
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_50_2020.tif
  format: null
  id: resource_4e68a8b5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_45_2020.tif
  format: null
  id: resource_a44fc2ba
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_40_2020.tif
  format: null
  id: resource_012253e3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_35_2020.tif
  format: null
  id: resource_624146cf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_30_2020.tif
  format: null
  id: resource_63121acb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_25_2020.tif
  format: null
  id: resource_0da29505
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_20_2020.tif
  format: null
  id: resource_e1d37b7f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_1_2020.tif
  format: null
  id: resource_6001f1e8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_15_2020.tif
  format: null
  id: resource_5f7caaff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_10_2020.tif
  format: null
  id: resource_ff54dbae
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/MNP/mnp_f_0_2020.tif
  format: null
  id: resource_d5c97225
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_80_2019.tif
  format: null
  id: resource_747a38e6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_75_2019.tif
  format: null
  id: resource_21007864
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_70_2019.tif
  format: null
  id: resource_ccbb94d1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_65_2019.tif
  format: null
  id: resource_f421c16b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_60_2019.tif
  format: null
  id: resource_d926557f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_5_2019.tif
  format: null
  id: resource_15e6de69
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_55_2019.tif
  format: null
  id: resource_543cd3e2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_50_2019.tif
  format: null
  id: resource_32eebc8b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_45_2019.tif
  format: null
  id: resource_529c7532
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_40_2019.tif
  format: null
  id: resource_86e01107
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_35_2019.tif
  format: null
  id: resource_4c11611f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_30_2019.tif
  format: null
  id: resource_9995dbe5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_25_2019.tif
  format: null
  id: resource_45a36e28
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_20_2019.tif
  format: null
  id: resource_d7bf24af
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_1_2019.tif
  format: null
  id: resource_688a07da
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_15_2019.tif
  format: null
  id: resource_d4a2d97d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_10_2019.tif
  format: null
  id: resource_1cd21bcc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_m_0_2019.tif
  format: null
  id: resource_1ed57b02
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_80_2019.tif
  format: null
  id: resource_4b8fb81c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_75_2019.tif
  format: null
  id: resource_045225c1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_70_2019.tif
  format: null
  id: resource_03b96d79
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_65_2019.tif
  format: null
  id: resource_6183f87a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_60_2019.tif
  format: null
  id: resource_148a1f4f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_5_2019.tif
  format: null
  id: resource_1e9786c8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_55_2019.tif
  format: null
  id: resource_7fc530e2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_50_2019.tif
  format: null
  id: resource_153f6282
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_45_2019.tif
  format: null
  id: resource_4c99f80a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_40_2019.tif
  format: null
  id: resource_54818d8a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_35_2019.tif
  format: null
  id: resource_5b91b68d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_30_2019.tif
  format: null
  id: resource_7b6eedb0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_25_2019.tif
  format: null
  id: resource_45500dab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_20_2019.tif
  format: null
  id: resource_443bde29
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_1_2019.tif
  format: null
  id: resource_ee33d7ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_15_2019.tif
  format: null
  id: resource_e94b3157
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_10_2019.tif
  format: null
  id: resource_c04c3680
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/MNP/mnp_f_0_2019.tif
  format: null
  id: resource_b5be4515
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_80_2018.tif
  format: null
  id: resource_6a743467
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_75_2018.tif
  format: null
  id: resource_11fe14a1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_70_2018.tif
  format: null
  id: resource_44236d7b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_65_2018.tif
  format: null
  id: resource_fd7955ea
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_60_2018.tif
  format: null
  id: resource_70899db6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_5_2018.tif
  format: null
  id: resource_0adc2127
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_55_2018.tif
  format: null
  id: resource_3be0098d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_50_2018.tif
  format: null
  id: resource_35b68e4d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_45_2018.tif
  format: null
  id: resource_2a695af5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_40_2018.tif
  format: null
  id: resource_9568e869
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_35_2018.tif
  format: null
  id: resource_0eb0d397
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_30_2018.tif
  format: null
  id: resource_1f58aedb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_25_2018.tif
  format: null
  id: resource_088b1850
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_20_2018.tif
  format: null
  id: resource_339aca5b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_1_2018.tif
  format: null
  id: resource_02703a2a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_15_2018.tif
  format: null
  id: resource_c4919e7a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_10_2018.tif
  format: null
  id: resource_42397b6e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_m_0_2018.tif
  format: null
  id: resource_938638f1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_80_2018.tif
  format: null
  id: resource_e87e5813
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_75_2018.tif
  format: null
  id: resource_c79b580f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_70_2018.tif
  format: null
  id: resource_4068b193
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_65_2018.tif
  format: null
  id: resource_4f29ee00
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_60_2018.tif
  format: null
  id: resource_88cdfac6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_5_2018.tif
  format: null
  id: resource_374c789c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_55_2018.tif
  format: null
  id: resource_4a574c74
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_50_2018.tif
  format: null
  id: resource_ac13066b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_45_2018.tif
  format: null
  id: resource_d15f2b16
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_40_2018.tif
  format: null
  id: resource_6f024b89
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_35_2018.tif
  format: null
  id: resource_77a2224b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_30_2018.tif
  format: null
  id: resource_45782977
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_25_2018.tif
  format: null
  id: resource_5d8ee3cf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_20_2018.tif
  format: null
  id: resource_9c171f73
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_1_2018.tif
  format: null
  id: resource_a95eba13
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_15_2018.tif
  format: null
  id: resource_093fe5e8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_10_2018.tif
  format: null
  id: resource_82a61dfb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/MNP/mnp_f_0_2018.tif
  format: null
  id: resource_2d30b4c5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_80_2017.tif
  format: null
  id: resource_e7d07ec4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_75_2017.tif
  format: null
  id: resource_341b3521
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_70_2017.tif
  format: null
  id: resource_7a59c217
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_65_2017.tif
  format: null
  id: resource_3dd14fad
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_60_2017.tif
  format: null
  id: resource_fd291fcf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_5_2017.tif
  format: null
  id: resource_33ecf824
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_55_2017.tif
  format: null
  id: resource_bf70f021
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_50_2017.tif
  format: null
  id: resource_65c1b099
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_45_2017.tif
  format: null
  id: resource_79e63657
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_40_2017.tif
  format: null
  id: resource_79eac6db
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_35_2017.tif
  format: null
  id: resource_b54abb6a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_30_2017.tif
  format: null
  id: resource_4dc1b5a9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_25_2017.tif
  format: null
  id: resource_ea35218d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_20_2017.tif
  format: null
  id: resource_0a770937
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_1_2017.tif
  format: null
  id: resource_33ae224c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_15_2017.tif
  format: null
  id: resource_dd74dd6d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_10_2017.tif
  format: null
  id: resource_91e97dc0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_m_0_2017.tif
  format: null
  id: resource_3aabb84a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_80_2017.tif
  format: null
  id: resource_945a6c66
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_75_2017.tif
  format: null
  id: resource_b86ef73f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_70_2017.tif
  format: null
  id: resource_c47d636b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_65_2017.tif
  format: null
  id: resource_b1226e84
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_60_2017.tif
  format: null
  id: resource_cd717bb7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_5_2017.tif
  format: null
  id: resource_78808e6c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_55_2017.tif
  format: null
  id: resource_bd6e983c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_50_2017.tif
  format: null
  id: resource_d0416319
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_45_2017.tif
  format: null
  id: resource_ff6e2c55
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_40_2017.tif
  format: null
  id: resource_de0ee3d6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_35_2017.tif
  format: null
  id: resource_4a083889
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_30_2017.tif
  format: null
  id: resource_2d0d536d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_25_2017.tif
  format: null
  id: resource_7c4859ab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_20_2017.tif
  format: null
  id: resource_1add4f03
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_1_2017.tif
  format: null
  id: resource_f6f29350
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_15_2017.tif
  format: null
  id: resource_a5294125
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_10_2017.tif
  format: null
  id: resource_896bffde
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/MNP/mnp_f_0_2017.tif
  format: null
  id: resource_7610cd6a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_80_2016.tif
  format: null
  id: resource_804512ab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_75_2016.tif
  format: null
  id: resource_0633ab15
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_70_2016.tif
  format: null
  id: resource_c5c873ba
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_65_2016.tif
  format: null
  id: resource_06d0bcfc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_60_2016.tif
  format: null
  id: resource_dc6a3e13
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_5_2016.tif
  format: null
  id: resource_ebc12bfc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_55_2016.tif
  format: null
  id: resource_08dba0bd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_50_2016.tif
  format: null
  id: resource_8f339615
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_45_2016.tif
  format: null
  id: resource_8e9b91d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_40_2016.tif
  format: null
  id: resource_af1eb549
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_35_2016.tif
  format: null
  id: resource_40ba3ee8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_30_2016.tif
  format: null
  id: resource_173204ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_25_2016.tif
  format: null
  id: resource_b6cb86d2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_20_2016.tif
  format: null
  id: resource_1322b8fe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_1_2016.tif
  format: null
  id: resource_90e2fcfa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_15_2016.tif
  format: null
  id: resource_c3a589fa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_10_2016.tif
  format: null
  id: resource_9de8e346
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_m_0_2016.tif
  format: null
  id: resource_52428697
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_m_0_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_80_2016.tif
  format: null
  id: resource_c78bfc27
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_75_2016.tif
  format: null
  id: resource_28128d59
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_70_2016.tif
  format: null
  id: resource_34313348
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_65_2016.tif
  format: null
  id: resource_bd339db6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_60_2016.tif
  format: null
  id: resource_96cfa9b3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_5_2016.tif
  format: null
  id: resource_2491dde8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_55_2016.tif
  format: null
  id: resource_8d1404c5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_50_2016.tif
  format: null
  id: resource_02dd132b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_45_2016.tif
  format: null
  id: resource_64278148
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_40_2016.tif
  format: null
  id: resource_25f9794d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_35_2016.tif
  format: null
  id: resource_52d8b424
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_30_2016.tif
  format: null
  id: resource_a93d30fd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_25_2016.tif
  format: null
  id: resource_06cafa23
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_20_2016.tif
  format: null
  id: resource_f1948ccc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_1_2016.tif
  format: null
  id: resource_d51f8b4b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_15_2016.tif
  format: null
  id: resource_a54e13c5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_10_2016.tif
  format: null
  id: resource_9f97822c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/MNP/mnp_f_0_2016.tif
  format: null
  id: resource_0da30dcf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_f_0_2016.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mnp_worldpop_northernmarianaislandsage_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - MNP
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Northern Mariana Islands - Age and gender structures
version: null
vulnerability: null
---
