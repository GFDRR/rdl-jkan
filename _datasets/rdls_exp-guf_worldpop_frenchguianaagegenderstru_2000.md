---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-french-guiana
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-french-guiana
dataset_id: rdls_exp-guf_worldpop_frenchguianaagegenderstru_2000
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
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-french-guiana]'
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
    counts by age group and gender at 3 arc-second resolution (~100m) for French Guiana
    in 2020. The dataset provides 180 GeoTIFF rasters representing population counts
    for each age-gender cohort.
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-french-guiana
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
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_80_2020.tif
  format: null
  id: resource_d8b7ef1d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_75_2020.tif
  format: null
  id: resource_36f6c6ff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_70_2020.tif
  format: null
  id: resource_1635c1ce
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_65_2020.tif
  format: null
  id: resource_80e636ce
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_60_2020.tif
  format: null
  id: resource_9618e3ed
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_5_2020.tif
  format: null
  id: resource_a9729757
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_55_2020.tif
  format: null
  id: resource_ec113d8e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_50_2020.tif
  format: null
  id: resource_07420d1a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_45_2020.tif
  format: null
  id: resource_a48f3e63
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_40_2020.tif
  format: null
  id: resource_958aea54
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_35_2020.tif
  format: null
  id: resource_1834d9cd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_30_2020.tif
  format: null
  id: resource_aaac4586
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_25_2020.tif
  format: null
  id: resource_0495aac7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_20_2020.tif
  format: null
  id: resource_cb8ffdf5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_1_2020.tif
  format: null
  id: resource_dd4ef065
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_15_2020.tif
  format: null
  id: resource_68d2ef92
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_10_2020.tif
  format: null
  id: resource_fafbe700
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_m_0_2020.tif
  format: null
  id: resource_445278aa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_80_2020.tif
  format: null
  id: resource_5540a43b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_75_2020.tif
  format: null
  id: resource_70a85ca7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_70_2020.tif
  format: null
  id: resource_99793684
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_65_2020.tif
  format: null
  id: resource_c9d30d2b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_60_2020.tif
  format: null
  id: resource_4d325a28
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_5_2020.tif
  format: null
  id: resource_445bb331
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_55_2020.tif
  format: null
  id: resource_82d695d0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_50_2020.tif
  format: null
  id: resource_2b13dfc4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_45_2020.tif
  format: null
  id: resource_2fc932d4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_40_2020.tif
  format: null
  id: resource_0014f24f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_35_2020.tif
  format: null
  id: resource_2badb302
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_30_2020.tif
  format: null
  id: resource_68f303a7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_25_2020.tif
  format: null
  id: resource_7e59bc1e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_20_2020.tif
  format: null
  id: resource_3ba5468f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_1_2020.tif
  format: null
  id: resource_dcd2f6fa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_15_2020.tif
  format: null
  id: resource_e2496646
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_10_2020.tif
  format: null
  id: resource_6e04221c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/GUF/guf_f_0_2020.tif
  format: null
  id: resource_f68bce27
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_80_2019.tif
  format: null
  id: resource_666b848d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_75_2019.tif
  format: null
  id: resource_e7c2a80f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_70_2019.tif
  format: null
  id: resource_a3d08e4b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_65_2019.tif
  format: null
  id: resource_64952e4f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_60_2019.tif
  format: null
  id: resource_5c54fd2a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_5_2019.tif
  format: null
  id: resource_80d0b82f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_55_2019.tif
  format: null
  id: resource_2d71d8b4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_50_2019.tif
  format: null
  id: resource_b8cfad75
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_45_2019.tif
  format: null
  id: resource_2837ca11
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_40_2019.tif
  format: null
  id: resource_aa7ff2d6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_35_2019.tif
  format: null
  id: resource_29f2ecbd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_30_2019.tif
  format: null
  id: resource_bf7b8de8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_25_2019.tif
  format: null
  id: resource_21841daf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_20_2019.tif
  format: null
  id: resource_7a2fcc42
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_1_2019.tif
  format: null
  id: resource_b6ec4e17
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_15_2019.tif
  format: null
  id: resource_0255b8bb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_10_2019.tif
  format: null
  id: resource_668ece9a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_m_0_2019.tif
  format: null
  id: resource_c3545814
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_80_2019.tif
  format: null
  id: resource_aaaeac4e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_75_2019.tif
  format: null
  id: resource_a736853a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_70_2019.tif
  format: null
  id: resource_19b32c91
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_65_2019.tif
  format: null
  id: resource_2c135b60
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_60_2019.tif
  format: null
  id: resource_cdecbaf2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_5_2019.tif
  format: null
  id: resource_a861a184
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_55_2019.tif
  format: null
  id: resource_58e00fca
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_50_2019.tif
  format: null
  id: resource_bb8ebc81
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_45_2019.tif
  format: null
  id: resource_fe6306cf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_40_2019.tif
  format: null
  id: resource_8589f8d4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_35_2019.tif
  format: null
  id: resource_b02c935e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_30_2019.tif
  format: null
  id: resource_d97e3b6a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_25_2019.tif
  format: null
  id: resource_a70a6564
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_20_2019.tif
  format: null
  id: resource_d2e3d58a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_1_2019.tif
  format: null
  id: resource_6a766333
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_15_2019.tif
  format: null
  id: resource_05036d00
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_10_2019.tif
  format: null
  id: resource_c3c0d85b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/GUF/guf_f_0_2019.tif
  format: null
  id: resource_b83731b6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_80_2018.tif
  format: null
  id: resource_36eef2d4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_75_2018.tif
  format: null
  id: resource_5bcc0875
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_70_2018.tif
  format: null
  id: resource_eca0040b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_65_2018.tif
  format: null
  id: resource_c71a44de
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_60_2018.tif
  format: null
  id: resource_22891458
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_5_2018.tif
  format: null
  id: resource_f59d2dab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_55_2018.tif
  format: null
  id: resource_20f607ec
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_50_2018.tif
  format: null
  id: resource_9ddd38e6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_45_2018.tif
  format: null
  id: resource_dbc61cd6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_40_2018.tif
  format: null
  id: resource_3cdb34b0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_35_2018.tif
  format: null
  id: resource_f1078390
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_30_2018.tif
  format: null
  id: resource_af852a87
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_25_2018.tif
  format: null
  id: resource_05a050b2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_20_2018.tif
  format: null
  id: resource_4e490a69
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_1_2018.tif
  format: null
  id: resource_275bcf74
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_15_2018.tif
  format: null
  id: resource_2a84cc37
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_10_2018.tif
  format: null
  id: resource_cc679150
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_m_0_2018.tif
  format: null
  id: resource_baf03fa2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_80_2018.tif
  format: null
  id: resource_e33cf555
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_75_2018.tif
  format: null
  id: resource_b838f3e4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_70_2018.tif
  format: null
  id: resource_44f01538
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_65_2018.tif
  format: null
  id: resource_9acc672a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_60_2018.tif
  format: null
  id: resource_178f9cc8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_5_2018.tif
  format: null
  id: resource_8d2d28ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_55_2018.tif
  format: null
  id: resource_283a8405
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_50_2018.tif
  format: null
  id: resource_a304f933
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_45_2018.tif
  format: null
  id: resource_3508ac11
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_40_2018.tif
  format: null
  id: resource_8ade6574
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_35_2018.tif
  format: null
  id: resource_9f065197
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_30_2018.tif
  format: null
  id: resource_647bea46
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_25_2018.tif
  format: null
  id: resource_3d684367
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_20_2018.tif
  format: null
  id: resource_e0ba382f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_1_2018.tif
  format: null
  id: resource_fadbee50
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_15_2018.tif
  format: null
  id: resource_07c9324b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_10_2018.tif
  format: null
  id: resource_b3fb0982
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/GUF/guf_f_0_2018.tif
  format: null
  id: resource_7cc2d16a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_80_2017.tif
  format: null
  id: resource_1a84e8a7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_75_2017.tif
  format: null
  id: resource_e4d767d4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_70_2017.tif
  format: null
  id: resource_86f77739
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_65_2017.tif
  format: null
  id: resource_f0c73a13
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_60_2017.tif
  format: null
  id: resource_7a893caa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_5_2017.tif
  format: null
  id: resource_e3c096ff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_55_2017.tif
  format: null
  id: resource_1291a98d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_50_2017.tif
  format: null
  id: resource_9661ccd8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_45_2017.tif
  format: null
  id: resource_74661615
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_40_2017.tif
  format: null
  id: resource_cf7090ba
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_35_2017.tif
  format: null
  id: resource_83e0779a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_30_2017.tif
  format: null
  id: resource_c370746a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_25_2017.tif
  format: null
  id: resource_7104cb76
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_20_2017.tif
  format: null
  id: resource_1602007f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_1_2017.tif
  format: null
  id: resource_26473660
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_15_2017.tif
  format: null
  id: resource_7bc830d4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_10_2017.tif
  format: null
  id: resource_87856fd0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_m_0_2017.tif
  format: null
  id: resource_68c805fb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_80_2017.tif
  format: null
  id: resource_229dd614
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_75_2017.tif
  format: null
  id: resource_27a6ef88
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_70_2017.tif
  format: null
  id: resource_e1983165
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_65_2017.tif
  format: null
  id: resource_adb7f348
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_60_2017.tif
  format: null
  id: resource_f6af4d35
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_5_2017.tif
  format: null
  id: resource_2c35d081
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_55_2017.tif
  format: null
  id: resource_959a96ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_50_2017.tif
  format: null
  id: resource_5678a109
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_45_2017.tif
  format: null
  id: resource_5e052ec6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_40_2017.tif
  format: null
  id: resource_e07b6d16
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_35_2017.tif
  format: null
  id: resource_bf8f4680
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_30_2017.tif
  format: null
  id: resource_914a9032
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_25_2017.tif
  format: null
  id: resource_73dcf3fa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_20_2017.tif
  format: null
  id: resource_c94e8f5b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_1_2017.tif
  format: null
  id: resource_2d299e00
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_15_2017.tif
  format: null
  id: resource_741f7a57
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_10_2017.tif
  format: null
  id: resource_07da0689
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/GUF/guf_f_0_2017.tif
  format: null
  id: resource_7d0f07a7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_80_2016.tif
  format: null
  id: resource_a516b7d1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_75_2016.tif
  format: null
  id: resource_7f7ccecb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_70_2016.tif
  format: null
  id: resource_2b7b0c08
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_65_2016.tif
  format: null
  id: resource_61b22c2a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_60_2016.tif
  format: null
  id: resource_0277ee25
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_5_2016.tif
  format: null
  id: resource_afd1ecaa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_55_2016.tif
  format: null
  id: resource_733b68d8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_50_2016.tif
  format: null
  id: resource_c0a8ff53
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_45_2016.tif
  format: null
  id: resource_d70f5802
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_40_2016.tif
  format: null
  id: resource_145000d9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_35_2016.tif
  format: null
  id: resource_aeafd33a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_30_2016.tif
  format: null
  id: resource_b92bdf24
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_25_2016.tif
  format: null
  id: resource_22c4c987
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_20_2016.tif
  format: null
  id: resource_9dbe8f2d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_1_2016.tif
  format: null
  id: resource_7d3d9b20
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_15_2016.tif
  format: null
  id: resource_0a84fc7f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_10_2016.tif
  format: null
  id: resource_f7501296
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_m_0_2016.tif
  format: null
  id: resource_5710f1fe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_m_0_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_80_2016.tif
  format: null
  id: resource_f6988d3e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_75_2016.tif
  format: null
  id: resource_3f1a1d3f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_70_2016.tif
  format: null
  id: resource_f8715fac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_65_2016.tif
  format: null
  id: resource_a71391af
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_60_2016.tif
  format: null
  id: resource_d97c234d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_5_2016.tif
  format: null
  id: resource_1e8406f0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_55_2016.tif
  format: null
  id: resource_4ecff434
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_50_2016.tif
  format: null
  id: resource_0c5a507d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_45_2016.tif
  format: null
  id: resource_c291df1f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_40_2016.tif
  format: null
  id: resource_44121f15
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_35_2016.tif
  format: null
  id: resource_e2499617
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_30_2016.tif
  format: null
  id: resource_f0fd0028
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_25_2016.tif
  format: null
  id: resource_f1e9681c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_20_2016.tif
  format: null
  id: resource_014b337e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_1_2016.tif
  format: null
  id: resource_0f435316
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_15_2016.tif
  format: null
  id: resource_f0084069
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_10_2016.tif
  format: null
  id: resource_a49ca341
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: French Guiana - Age and gender structures (French Guiana 100m Age structures
    in 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/GUF/guf_f_0_2016.tif
  format: null
  id: resource_b59cfb6c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: guf_f_0_2016.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-guf_worldpop_frenchguianaagegenderstru_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - GUF
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: French Guiana - Age and gender structures
version: null
vulnerability: null
---
