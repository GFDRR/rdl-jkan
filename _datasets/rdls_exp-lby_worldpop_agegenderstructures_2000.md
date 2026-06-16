---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop, University of Southampton
    url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-libya
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-libya
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-libya
dataset_id: rdls_exp-lby_worldpop_agegenderstructures_2000
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
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-libya]'
details: null
exposure:
- asset_type:
    description: Gridded population counts for Libya disaggregated by gender and 5-year
      age groups (0-1, 5-year bands up to 80+) at approximately 100m resolution for
      2020
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
  description: Age- and gender-disaggregated population estimates for Libya were generated
    by WorldPop using a modelling approach that combines census-derived demographic
    structures with gridded total population counts, distributing population into
    gender and 5-year age bands across a 3 arc-second (~100m) raster grid for the
    reference year 2020. The methodology follows Tatem et al. (2013) and Pezzulo et
    al. (2017), applying dasymetric mapping and statistical downscaling techniques.
    The resulting GeoTIFF layers support disaster risk assessments requiring age-
    and gender-sensitive exposure analysis.
  sources:
  - id: source_1
    license: null
    name: WorldPop, University of Southampton
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-libya
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
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_80_2020.tif
  format: null
  id: resource_8e05c1e4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_75_2020.tif
  format: null
  id: resource_1ce24704
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_70_2020.tif
  format: null
  id: resource_5728122a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_65_2020.tif
  format: null
  id: resource_5b978451
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_60_2020.tif
  format: null
  id: resource_669f9655
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_5_2020.tif
  format: null
  id: resource_951973e6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_55_2020.tif
  format: null
  id: resource_76032435
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_50_2020.tif
  format: null
  id: resource_8e6003d9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_45_2020.tif
  format: null
  id: resource_4a0ea87f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_40_2020.tif
  format: null
  id: resource_b57b4512
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_35_2020.tif
  format: null
  id: resource_3b160d4d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_30_2020.tif
  format: null
  id: resource_9ecf02e3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_25_2020.tif
  format: null
  id: resource_9257f31c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_20_2020.tif
  format: null
  id: resource_b4b8156c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_1_2020.tif
  format: null
  id: resource_426e063f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_15_2020.tif
  format: null
  id: resource_10d9d76f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_10_2020.tif
  format: null
  id: resource_0489daf6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_m_0_2020.tif
  format: null
  id: resource_b9634e83
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_80_2020.tif
  format: null
  id: resource_16688ed4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_75_2020.tif
  format: null
  id: resource_d75a0a10
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_70_2020.tif
  format: null
  id: resource_88c87d27
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_65_2020.tif
  format: null
  id: resource_ca2336e1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_60_2020.tif
  format: null
  id: resource_f97225c7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_5_2020.tif
  format: null
  id: resource_a61aa565
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_55_2020.tif
  format: null
  id: resource_efb1fe92
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_50_2020.tif
  format: null
  id: resource_1f40d4a5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_45_2020.tif
  format: null
  id: resource_ad4915aa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_40_2020.tif
  format: null
  id: resource_85e684e6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_35_2020.tif
  format: null
  id: resource_5b6b255a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_30_2020.tif
  format: null
  id: resource_adfccace
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_25_2020.tif
  format: null
  id: resource_96c9ee5f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_20_2020.tif
  format: null
  id: resource_b461fd84
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_1_2020.tif
  format: null
  id: resource_ee7e09d6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_15_2020.tif
  format: null
  id: resource_9b14fb77
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_10_2020.tif
  format: null
  id: resource_f1e4727c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/LBY/lby_f_0_2020.tif
  format: null
  id: resource_f49f62b4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_80_2019.tif
  format: null
  id: resource_2e1326b9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_75_2019.tif
  format: null
  id: resource_c812ed1a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_70_2019.tif
  format: null
  id: resource_284c461c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_65_2019.tif
  format: null
  id: resource_3d4195ad
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_60_2019.tif
  format: null
  id: resource_b1dae717
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_5_2019.tif
  format: null
  id: resource_3e0a37ce
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_55_2019.tif
  format: null
  id: resource_a48f6621
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_50_2019.tif
  format: null
  id: resource_79d3e714
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_45_2019.tif
  format: null
  id: resource_3a5a9c38
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_40_2019.tif
  format: null
  id: resource_50bd55ce
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_35_2019.tif
  format: null
  id: resource_38078213
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_30_2019.tif
  format: null
  id: resource_c6ae4129
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_25_2019.tif
  format: null
  id: resource_6f8c42e7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_20_2019.tif
  format: null
  id: resource_f7192ac8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_1_2019.tif
  format: null
  id: resource_47442f44
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_15_2019.tif
  format: null
  id: resource_43b6e95d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_10_2019.tif
  format: null
  id: resource_4157c4a9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_m_0_2019.tif
  format: null
  id: resource_c5d457c2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_80_2019.tif
  format: null
  id: resource_91e1391d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_75_2019.tif
  format: null
  id: resource_13149517
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_70_2019.tif
  format: null
  id: resource_7490ff67
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_65_2019.tif
  format: null
  id: resource_1ddadb9f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_60_2019.tif
  format: null
  id: resource_3c571991
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_5_2019.tif
  format: null
  id: resource_faf89de8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_55_2019.tif
  format: null
  id: resource_7f216af2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_50_2019.tif
  format: null
  id: resource_453419a3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_45_2019.tif
  format: null
  id: resource_84b6d811
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_40_2019.tif
  format: null
  id: resource_8788e113
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_35_2019.tif
  format: null
  id: resource_d75fcced
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_30_2019.tif
  format: null
  id: resource_af9a9152
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_25_2019.tif
  format: null
  id: resource_b4e9b199
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_20_2019.tif
  format: null
  id: resource_9d0b0a67
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_1_2019.tif
  format: null
  id: resource_aff2713b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_15_2019.tif
  format: null
  id: resource_f280a6de
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_10_2019.tif
  format: null
  id: resource_df57622f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/LBY/lby_f_0_2019.tif
  format: null
  id: resource_806da951
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_80_2018.tif
  format: null
  id: resource_3881b661
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_75_2018.tif
  format: null
  id: resource_2a0c7a09
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_70_2018.tif
  format: null
  id: resource_c7968f11
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_65_2018.tif
  format: null
  id: resource_780cf3c4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_60_2018.tif
  format: null
  id: resource_30e732d9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_5_2018.tif
  format: null
  id: resource_ebe27e38
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_55_2018.tif
  format: null
  id: resource_745c4597
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_50_2018.tif
  format: null
  id: resource_acd77812
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_45_2018.tif
  format: null
  id: resource_3ebc9624
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_40_2018.tif
  format: null
  id: resource_5f483714
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_35_2018.tif
  format: null
  id: resource_83403d56
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_30_2018.tif
  format: null
  id: resource_ac224966
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_25_2018.tif
  format: null
  id: resource_a0d6b8f1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_20_2018.tif
  format: null
  id: resource_c67fb4fd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_1_2018.tif
  format: null
  id: resource_2f49b63a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_15_2018.tif
  format: null
  id: resource_b81ac1dc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_10_2018.tif
  format: null
  id: resource_bb6a84ca
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_m_0_2018.tif
  format: null
  id: resource_b713e69a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_80_2018.tif
  format: null
  id: resource_dd7b2609
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_75_2018.tif
  format: null
  id: resource_21989d07
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_70_2018.tif
  format: null
  id: resource_66791b77
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_65_2018.tif
  format: null
  id: resource_dce47585
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_60_2018.tif
  format: null
  id: resource_f082333c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_5_2018.tif
  format: null
  id: resource_092b6334
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_55_2018.tif
  format: null
  id: resource_2f3a6cf7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_50_2018.tif
  format: null
  id: resource_ff77b18b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_45_2018.tif
  format: null
  id: resource_fface58d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_40_2018.tif
  format: null
  id: resource_2e0616eb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_35_2018.tif
  format: null
  id: resource_d7cf4b9d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_30_2018.tif
  format: null
  id: resource_d49c0bb2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_25_2018.tif
  format: null
  id: resource_69edc6a2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_20_2018.tif
  format: null
  id: resource_674f9a66
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_1_2018.tif
  format: null
  id: resource_3cf624e8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_15_2018.tif
  format: null
  id: resource_2d5f4074
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_10_2018.tif
  format: null
  id: resource_e14fb2a7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/LBY/lby_f_0_2018.tif
  format: null
  id: resource_3c9298b1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_80_2017.tif
  format: null
  id: resource_3373957e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_75_2017.tif
  format: null
  id: resource_1dbf2e99
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_70_2017.tif
  format: null
  id: resource_030ef94b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_65_2017.tif
  format: null
  id: resource_00e04f95
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_60_2017.tif
  format: null
  id: resource_6aa1acf6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_5_2017.tif
  format: null
  id: resource_7c6961a9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_55_2017.tif
  format: null
  id: resource_6a5491e8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_50_2017.tif
  format: null
  id: resource_21f964b8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_45_2017.tif
  format: null
  id: resource_f7d1f86f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_40_2017.tif
  format: null
  id: resource_8c69f862
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_35_2017.tif
  format: null
  id: resource_f1dd1b1e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_30_2017.tif
  format: null
  id: resource_c60dadee
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_25_2017.tif
  format: null
  id: resource_31142af5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_20_2017.tif
  format: null
  id: resource_8385465b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_1_2017.tif
  format: null
  id: resource_520f413f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_15_2017.tif
  format: null
  id: resource_1e377e3f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_10_2017.tif
  format: null
  id: resource_f0aef989
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_m_0_2017.tif
  format: null
  id: resource_c278019d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_80_2017.tif
  format: null
  id: resource_a5845f01
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_75_2017.tif
  format: null
  id: resource_4d7d3a92
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_70_2017.tif
  format: null
  id: resource_e5503839
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_65_2017.tif
  format: null
  id: resource_68cce384
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_60_2017.tif
  format: null
  id: resource_0aa2bc9a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_5_2017.tif
  format: null
  id: resource_62432707
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_55_2017.tif
  format: null
  id: resource_d104f33b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_50_2017.tif
  format: null
  id: resource_31c8f28c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_45_2017.tif
  format: null
  id: resource_99a84195
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_40_2017.tif
  format: null
  id: resource_a1e5d639
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_35_2017.tif
  format: null
  id: resource_29ff0eda
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_30_2017.tif
  format: null
  id: resource_1aa0c9a1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_25_2017.tif
  format: null
  id: resource_bceee96d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_20_2017.tif
  format: null
  id: resource_39b2ce7d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_1_2017.tif
  format: null
  id: resource_f962486d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_15_2017.tif
  format: null
  id: resource_bac51ac6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_10_2017.tif
  format: null
  id: resource_96f0ab52
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/LBY/lby_f_0_2017.tif
  format: null
  id: resource_25862c8b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_80_2016.tif
  format: null
  id: resource_b032bdae
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_75_2016.tif
  format: null
  id: resource_871ebcf1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_70_2016.tif
  format: null
  id: resource_9c944a98
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_65_2016.tif
  format: null
  id: resource_b9a0cd68
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_60_2016.tif
  format: null
  id: resource_77b86303
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_5_2016.tif
  format: null
  id: resource_8cd36afb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_55_2016.tif
  format: null
  id: resource_4871117d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_50_2016.tif
  format: null
  id: resource_807bdbf9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_45_2016.tif
  format: null
  id: resource_b0be1b10
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_40_2016.tif
  format: null
  id: resource_a293e991
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_35_2016.tif
  format: null
  id: resource_55105a18
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_30_2016.tif
  format: null
  id: resource_b2682df7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_25_2016.tif
  format: null
  id: resource_6dc40123
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_20_2016.tif
  format: null
  id: resource_9274fe2e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_1_2016.tif
  format: null
  id: resource_51b2f1fc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_15_2016.tif
  format: null
  id: resource_6b7f261f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_10_2016.tif
  format: null
  id: resource_0aa5af03
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_m_0_2016.tif
  format: null
  id: resource_80434ec1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_m_0_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_80_2016.tif
  format: null
  id: resource_574e2df3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_75_2016.tif
  format: null
  id: resource_cc7b0c87
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_70_2016.tif
  format: null
  id: resource_b9d3d2b9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_65_2016.tif
  format: null
  id: resource_49862546
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_60_2016.tif
  format: null
  id: resource_9125aff4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_5_2016.tif
  format: null
  id: resource_6fe8b0eb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_55_2016.tif
  format: null
  id: resource_0bde52b1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_50_2016.tif
  format: null
  id: resource_088a7c58
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_45_2016.tif
  format: null
  id: resource_3887680c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_40_2016.tif
  format: null
  id: resource_43ac632c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_35_2016.tif
  format: null
  id: resource_b790674a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_30_2016.tif
  format: null
  id: resource_76c5cfa6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_25_2016.tif
  format: null
  id: resource_c1102998
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_20_2016.tif
  format: null
  id: resource_97643cf7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_1_2016.tif
  format: null
  id: resource_6e70d858
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_15_2016.tif
  format: null
  id: resource_85658dcb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_10_2016.tif
  format: null
  id: resource_51441d9c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Libya - Age and gender structures (Libya 100m Age structures in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/LBY/lby_f_0_2016.tif
  format: null
  id: resource_266ae705
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: lby_f_0_2016.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-lby_worldpop_agegenderstructures_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - LBY
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Libya - Age and gender structures
version: null
vulnerability: null
---
