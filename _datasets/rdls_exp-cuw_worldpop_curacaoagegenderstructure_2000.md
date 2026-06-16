---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-curacao
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-curacao
dataset_id: rdls_exp-cuw_worldpop_curacaoagegenderstructure_2000
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
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-curacao]'
details: null
exposure:
- asset_type:
    description: Gridded population counts disaggregated by age group (0-1, 5-year
      bands to 80+) and gender at 100m resolution for 2020
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
license: CC-BY-4.0
lineage:
  description: "WorldPop applied spatial disaggregation methods (Tatem et al., Pezzulo\
    \ et al.) to census and survey population data to produce age-gender stratified\
    \ population counts at 100m grid resolution. The dataset provides estimates of\
    \ total people per grid cell broken down by gender and 5-year age bands for 2020\
    \ in Cura\xE7ao."
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-curacao
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
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_80_2020.tif
  format: null
  id: resource_afc45db0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_75_2020.tif
  format: null
  id: resource_dc440997
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_70_2020.tif
  format: null
  id: resource_ea98830c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_65_2020.tif
  format: null
  id: resource_20f85c63
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_60_2020.tif
  format: null
  id: resource_ff11d092
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_5_2020.tif
  format: null
  id: resource_7622d54a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_55_2020.tif
  format: null
  id: resource_646b92a6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_50_2020.tif
  format: null
  id: resource_ebfd14ad
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_45_2020.tif
  format: null
  id: resource_0e656450
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_40_2020.tif
  format: null
  id: resource_e632556d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_35_2020.tif
  format: null
  id: resource_9bea7a01
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_30_2020.tif
  format: null
  id: resource_0cf43ed7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_25_2020.tif
  format: null
  id: resource_c2fad4d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_20_2020.tif
  format: null
  id: resource_e474caaf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_1_2020.tif
  format: null
  id: resource_f5b85968
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_15_2020.tif
  format: null
  id: resource_854973b4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_10_2020.tif
  format: null
  id: resource_1ce93088
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_m_0_2020.tif
  format: null
  id: resource_270017ff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_80_2020.tif
  format: null
  id: resource_0d9d27b9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_75_2020.tif
  format: null
  id: resource_046789de
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_70_2020.tif
  format: null
  id: resource_51e83438
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_65_2020.tif
  format: null
  id: resource_926161fb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_60_2020.tif
  format: null
  id: resource_6bbeaaab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_5_2020.tif
  format: null
  id: resource_c57eab1e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_55_2020.tif
  format: null
  id: resource_753a40d1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_50_2020.tif
  format: null
  id: resource_a0fae59b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_45_2020.tif
  format: null
  id: resource_4c019e5d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_40_2020.tif
  format: null
  id: resource_9232a97e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_35_2020.tif
  format: null
  id: resource_aa9ad24b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_30_2020.tif
  format: null
  id: resource_c3a55e0c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_25_2020.tif
  format: null
  id: resource_25630ef5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_20_2020.tif
  format: null
  id: resource_9e26068d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_1_2020.tif
  format: null
  id: resource_b67a4f6b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_15_2020.tif
  format: null
  id: resource_a4517220
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_10_2020.tif
  format: null
  id: resource_62a62ce3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2020)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/CUW/cuw_f_0_2020.tif
  format: null
  id: resource_9c25a849
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_80_2019.tif
  format: null
  id: resource_71a17cdd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_75_2019.tif
  format: null
  id: resource_3e8d159d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_70_2019.tif
  format: null
  id: resource_97a8eae7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_65_2019.tif
  format: null
  id: resource_37cff882
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_60_2019.tif
  format: null
  id: resource_1fed19d6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_5_2019.tif
  format: null
  id: resource_bb5a4d66
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_55_2019.tif
  format: null
  id: resource_dc50617e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_50_2019.tif
  format: null
  id: resource_36f7d2d4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_45_2019.tif
  format: null
  id: resource_2d85da75
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_40_2019.tif
  format: null
  id: resource_4c50cc7a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_35_2019.tif
  format: null
  id: resource_4fabb15b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_30_2019.tif
  format: null
  id: resource_ad92742c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_25_2019.tif
  format: null
  id: resource_ed3fe4a5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_20_2019.tif
  format: null
  id: resource_ce1116d7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_1_2019.tif
  format: null
  id: resource_bb192d0f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_15_2019.tif
  format: null
  id: resource_688d84df
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_10_2019.tif
  format: null
  id: resource_72d69e04
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_m_0_2019.tif
  format: null
  id: resource_7a5055cf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_80_2019.tif
  format: null
  id: resource_b0ba8edd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_75_2019.tif
  format: null
  id: resource_3f78e17e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_70_2019.tif
  format: null
  id: resource_f143eca0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_65_2019.tif
  format: null
  id: resource_f960680b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_60_2019.tif
  format: null
  id: resource_86cfeeb8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_5_2019.tif
  format: null
  id: resource_2d5b8d52
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_55_2019.tif
  format: null
  id: resource_80406ada
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_50_2019.tif
  format: null
  id: resource_4a3724c3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_45_2019.tif
  format: null
  id: resource_10b17bf0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_40_2019.tif
  format: null
  id: resource_8f9049f2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_35_2019.tif
  format: null
  id: resource_b5360566
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_30_2019.tif
  format: null
  id: resource_8938c0c2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_25_2019.tif
  format: null
  id: resource_6c1c6397
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_20_2019.tif
  format: null
  id: resource_e7b4c0e2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_1_2019.tif
  format: null
  id: resource_a9850718
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_15_2019.tif
  format: null
  id: resource_4c78f756
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_10_2019.tif
  format: null
  id: resource_0eddfc02
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2019)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/CUW/cuw_f_0_2019.tif
  format: null
  id: resource_8dd847e5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_80_2018.tif
  format: null
  id: resource_5ba8013f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_75_2018.tif
  format: null
  id: resource_5c5940c3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_70_2018.tif
  format: null
  id: resource_ce64e4c5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_65_2018.tif
  format: null
  id: resource_df3c47db
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_60_2018.tif
  format: null
  id: resource_f18cc618
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_5_2018.tif
  format: null
  id: resource_834ed408
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_55_2018.tif
  format: null
  id: resource_fabcb4bc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_50_2018.tif
  format: null
  id: resource_eac7f484
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_45_2018.tif
  format: null
  id: resource_b218f5f1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_40_2018.tif
  format: null
  id: resource_516f2acf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_35_2018.tif
  format: null
  id: resource_7d107eb3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_30_2018.tif
  format: null
  id: resource_724828c4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_25_2018.tif
  format: null
  id: resource_b55620ba
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_20_2018.tif
  format: null
  id: resource_16ad750b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_1_2018.tif
  format: null
  id: resource_c5f14588
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_15_2018.tif
  format: null
  id: resource_8ea753a1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_10_2018.tif
  format: null
  id: resource_0bf685f9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_m_0_2018.tif
  format: null
  id: resource_fc852715
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_80_2018.tif
  format: null
  id: resource_6a8013ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_75_2018.tif
  format: null
  id: resource_fcf8b056
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_70_2018.tif
  format: null
  id: resource_32d4180c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_65_2018.tif
  format: null
  id: resource_3df9a352
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_60_2018.tif
  format: null
  id: resource_de744b65
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_5_2018.tif
  format: null
  id: resource_9691f333
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_55_2018.tif
  format: null
  id: resource_1eca1a72
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_50_2018.tif
  format: null
  id: resource_baaa4ca7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_45_2018.tif
  format: null
  id: resource_bd13a085
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_40_2018.tif
  format: null
  id: resource_553ba1ff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_35_2018.tif
  format: null
  id: resource_be0d3835
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_30_2018.tif
  format: null
  id: resource_509c79ea
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_25_2018.tif
  format: null
  id: resource_f4ae8656
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_20_2018.tif
  format: null
  id: resource_22bc1cb2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_1_2018.tif
  format: null
  id: resource_ac1f5246
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_15_2018.tif
  format: null
  id: resource_26afa4c8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_10_2018.tif
  format: null
  id: resource_f6f16752
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2018)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/CUW/cuw_f_0_2018.tif
  format: null
  id: resource_5e7c4788
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_80_2017.tif
  format: null
  id: resource_3c9039df
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_75_2017.tif
  format: null
  id: resource_f3e2bb96
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_70_2017.tif
  format: null
  id: resource_8329e16d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_65_2017.tif
  format: null
  id: resource_5b2989a6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_60_2017.tif
  format: null
  id: resource_e33ef0c8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_5_2017.tif
  format: null
  id: resource_9cee7c2b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_55_2017.tif
  format: null
  id: resource_2c881a79
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_50_2017.tif
  format: null
  id: resource_fd0e9f4a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_45_2017.tif
  format: null
  id: resource_31e2f1dc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_40_2017.tif
  format: null
  id: resource_9714e625
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_35_2017.tif
  format: null
  id: resource_15d635b8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_30_2017.tif
  format: null
  id: resource_5206553b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_25_2017.tif
  format: null
  id: resource_1f845dd4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_20_2017.tif
  format: null
  id: resource_c38feaee
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_1_2017.tif
  format: null
  id: resource_5911e00c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_15_2017.tif
  format: null
  id: resource_4db85cb9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_10_2017.tif
  format: null
  id: resource_0dddeaf2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_m_0_2017.tif
  format: null
  id: resource_a7a612da
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_80_2017.tif
  format: null
  id: resource_b539c10b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_75_2017.tif
  format: null
  id: resource_a971c2f3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_70_2017.tif
  format: null
  id: resource_6b95d815
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_65_2017.tif
  format: null
  id: resource_a927d9e3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_60_2017.tif
  format: null
  id: resource_725f7c87
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_5_2017.tif
  format: null
  id: resource_daeeca9d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_55_2017.tif
  format: null
  id: resource_6fdf8d45
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_50_2017.tif
  format: null
  id: resource_da4e0627
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_45_2017.tif
  format: null
  id: resource_86ebb44a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_40_2017.tif
  format: null
  id: resource_ec2dccda
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_35_2017.tif
  format: null
  id: resource_b507190b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_30_2017.tif
  format: null
  id: resource_c86ae6d3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_25_2017.tif
  format: null
  id: resource_f30455b2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_20_2017.tif
  format: null
  id: resource_ec505f88
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_1_2017.tif
  format: null
  id: resource_617f9024
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_15_2017.tif
  format: null
  id: resource_05fbd8d6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_10_2017.tif
  format: null
  id: resource_f310c656
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2017)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/CUW/cuw_f_0_2017.tif
  format: null
  id: resource_a509822f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_80_2016.tif
  format: null
  id: resource_ddc2437f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_75_2016.tif
  format: null
  id: resource_269c0d93
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_70_2016.tif
  format: null
  id: resource_9c6a94f3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_65_2016.tif
  format: null
  id: resource_478aa465
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_60_2016.tif
  format: null
  id: resource_65b7f5fe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_5_2016.tif
  format: null
  id: resource_8fb68e92
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_55_2016.tif
  format: null
  id: resource_21b72ae4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_50_2016.tif
  format: null
  id: resource_77e5026a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_45_2016.tif
  format: null
  id: resource_39709b84
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_40_2016.tif
  format: null
  id: resource_7a5b0b01
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_35_2016.tif
  format: null
  id: resource_1e448b9c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_30_2016.tif
  format: null
  id: resource_a5a66c39
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_25_2016.tif
  format: null
  id: resource_0b1289a5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_20_2016.tif
  format: null
  id: resource_cb99d37f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_1_2016.tif
  format: null
  id: resource_69700129
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_15_2016.tif
  format: null
  id: resource_ad139f55
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_10_2016.tif
  format: null
  id: resource_d4196350
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_m_0_2016.tif
  format: null
  id: resource_e7b9829f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_m_0_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_80_2016.tif
  format: null
  id: resource_fda953c0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_75_2016.tif
  format: null
  id: resource_bc6fa0cd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_70_2016.tif
  format: null
  id: resource_a6830ae5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_65_2016.tif
  format: null
  id: resource_35e6c1de
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_60_2016.tif
  format: null
  id: resource_3b69e971
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_5_2016.tif
  format: null
  id: resource_13716bcc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_55_2016.tif
  format: null
  id: resource_fcbc807f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_50_2016.tif
  format: null
  id: resource_396624f9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_45_2016.tif
  format: null
  id: resource_100f15b9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_40_2016.tif
  format: null
  id: resource_c2207fa9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_35_2016.tif
  format: null
  id: resource_e1d1ed4c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_30_2016.tif
  format: null
  id: resource_39546d18
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_25_2016.tif
  format: null
  id: resource_958db00b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_20_2016.tif
  format: null
  id: resource_3773eeb4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_1_2016.tif
  format: null
  id: resource_80b19b24
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_15_2016.tif
  format: null
  id: resource_313ce526
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_10_2016.tif
  format: null
  id: resource_e2cfb8e8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: "Cura\xE7ao - Age and gender structures (Cura\xE7ao 100m Age structures\
    \ in 2016)"
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/CUW/cuw_f_0_2016.tif
  format: null
  id: resource_8eb4b146
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: cuw_f_0_2016.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-cuw_worldpop_curacaoagegenderstructure_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - CUW
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: "Cura\xE7ao - Age and gender structures"
version: null
vulnerability: null
---
