---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-bonaire-sint-eustatius-and-saba
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-bonaire-sint-eustatius-and-saba
dataset_id: rdls_exp-bes_worldpop_bonairesinteustatiussabaa_2000
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
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-bonaire-sint-eustatius-and-saba]'
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
    et al., Pezzulo et al.). The dataset provides raster layers at 3 arc-second resolution
    (~100m) for each age-gender cohort in 2020 for the Caribbean territories of Bonaire,
    Sint Eustatius, and Saba.
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-for-bonaire-sint-eustatius-and-saba
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
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_80_2020.tif
  format: null
  id: resource_61ca39e8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_75_2020.tif
  format: null
  id: resource_5d1f456e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_70_2020.tif
  format: null
  id: resource_683455aa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_65_2020.tif
  format: null
  id: resource_0eff7703
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_60_2020.tif
  format: null
  id: resource_66d8ea32
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_5_2020.tif
  format: null
  id: resource_55e265fc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_55_2020.tif
  format: null
  id: resource_f18b3a73
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_50_2020.tif
  format: null
  id: resource_9edcbffb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_45_2020.tif
  format: null
  id: resource_41fb1916
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_40_2020.tif
  format: null
  id: resource_f5417a55
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_35_2020.tif
  format: null
  id: resource_28f9bc74
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_30_2020.tif
  format: null
  id: resource_73b0ca1c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_25_2020.tif
  format: null
  id: resource_2efc2373
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_20_2020.tif
  format: null
  id: resource_a1b79c02
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_1_2020.tif
  format: null
  id: resource_cdb94631
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_15_2020.tif
  format: null
  id: resource_ba66bd4b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_10_2020.tif
  format: null
  id: resource_8e77889e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_m_0_2020.tif
  format: null
  id: resource_33c14134
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_80_2020.tif
  format: null
  id: resource_73100d19
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_80_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_75_2020.tif
  format: null
  id: resource_230ef16c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_75_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_70_2020.tif
  format: null
  id: resource_44f2521a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_70_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_65_2020.tif
  format: null
  id: resource_e6ea5eab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_65_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_60_2020.tif
  format: null
  id: resource_9afce372
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_60_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_5_2020.tif
  format: null
  id: resource_6fcd451f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_5_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_55_2020.tif
  format: null
  id: resource_d51709d3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_55_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_50_2020.tif
  format: null
  id: resource_a0ed9b54
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_50_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_45_2020.tif
  format: null
  id: resource_218aba8d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_45_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_40_2020.tif
  format: null
  id: resource_82a60038
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_40_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_35_2020.tif
  format: null
  id: resource_73bf801e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_35_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_30_2020.tif
  format: null
  id: resource_2b6b2fba
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_30_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_25_2020.tif
  format: null
  id: resource_b052b3e9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_25_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_20_2020.tif
  format: null
  id: resource_7e6bcfb4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_20_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_1_2020.tif
  format: null
  id: resource_9eb22233
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_1_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_15_2020.tif
  format: null
  id: resource_3a2b95f7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_15_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_10_2020.tif
  format: null
  id: resource_9f188da0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_10_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2020
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2020/BES/bes_f_0_2020.tif
  format: null
  id: resource_4818a904
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_0_2020.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_80_2019.tif
  format: null
  id: resource_613c4f27
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_75_2019.tif
  format: null
  id: resource_be4a6f9d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_70_2019.tif
  format: null
  id: resource_85c55864
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_65_2019.tif
  format: null
  id: resource_aaebf6ff
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_60_2019.tif
  format: null
  id: resource_cb88a4ca
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_5_2019.tif
  format: null
  id: resource_64f5b7f4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_55_2019.tif
  format: null
  id: resource_7c646adb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_50_2019.tif
  format: null
  id: resource_a9dd6c4f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_45_2019.tif
  format: null
  id: resource_2b63b820
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_40_2019.tif
  format: null
  id: resource_9ae2236e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_35_2019.tif
  format: null
  id: resource_c763daad
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_30_2019.tif
  format: null
  id: resource_e2d81ddd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_25_2019.tif
  format: null
  id: resource_1e3f8cc0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_20_2019.tif
  format: null
  id: resource_c86de5a7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_1_2019.tif
  format: null
  id: resource_b3dddd1d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_15_2019.tif
  format: null
  id: resource_73b2b450
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_10_2019.tif
  format: null
  id: resource_48d95677
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_m_0_2019.tif
  format: null
  id: resource_90a4fbaa
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_80_2019.tif
  format: null
  id: resource_9f466638
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_80_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_75_2019.tif
  format: null
  id: resource_cdcf89bd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_75_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_70_2019.tif
  format: null
  id: resource_0d06a4d6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_70_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_65_2019.tif
  format: null
  id: resource_4cc8b76e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_65_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_60_2019.tif
  format: null
  id: resource_900ddea2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_60_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_5_2019.tif
  format: null
  id: resource_fe1dd243
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_5_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_55_2019.tif
  format: null
  id: resource_b10fc0ae
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_55_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_50_2019.tif
  format: null
  id: resource_bc0eead0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_50_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_45_2019.tif
  format: null
  id: resource_32b4a0e0
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_45_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_40_2019.tif
  format: null
  id: resource_0d9d228e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_40_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_35_2019.tif
  format: null
  id: resource_8a62f7af
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_35_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_30_2019.tif
  format: null
  id: resource_13ab32f8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_30_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_25_2019.tif
  format: null
  id: resource_8355c452
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_25_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_20_2019.tif
  format: null
  id: resource_28b47ec5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_20_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_1_2019.tif
  format: null
  id: resource_faa9bb8a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_1_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_15_2019.tif
  format: null
  id: resource_07039267
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_15_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_10_2019.tif
  format: null
  id: resource_7df6f9f1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_10_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2019
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2019/BES/bes_f_0_2019.tif
  format: null
  id: resource_5e3cb869
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_0_2019.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_80_2018.tif
  format: null
  id: resource_82139c70
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_75_2018.tif
  format: null
  id: resource_9d58233a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_70_2018.tif
  format: null
  id: resource_410b7c6e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_65_2018.tif
  format: null
  id: resource_5b59c401
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_60_2018.tif
  format: null
  id: resource_75e23337
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_5_2018.tif
  format: null
  id: resource_7e904e4d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_55_2018.tif
  format: null
  id: resource_7eeb2ab4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_50_2018.tif
  format: null
  id: resource_82574494
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_45_2018.tif
  format: null
  id: resource_5ec2820a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_40_2018.tif
  format: null
  id: resource_9fc75a9b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_35_2018.tif
  format: null
  id: resource_73b74b93
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_30_2018.tif
  format: null
  id: resource_12e047be
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_25_2018.tif
  format: null
  id: resource_5e4906e4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_20_2018.tif
  format: null
  id: resource_b708c01b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_1_2018.tif
  format: null
  id: resource_4eca3dfe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_15_2018.tif
  format: null
  id: resource_8f46467f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_10_2018.tif
  format: null
  id: resource_c875c1d9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_m_0_2018.tif
  format: null
  id: resource_4b4901db
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_80_2018.tif
  format: null
  id: resource_f60e4938
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_80_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_75_2018.tif
  format: null
  id: resource_3802c012
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_75_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_70_2018.tif
  format: null
  id: resource_b7646683
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_70_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_65_2018.tif
  format: null
  id: resource_f65467f4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_65_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_60_2018.tif
  format: null
  id: resource_b4d3ad54
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_60_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_5_2018.tif
  format: null
  id: resource_4727ef57
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_5_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_55_2018.tif
  format: null
  id: resource_ce5e35a9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_55_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_50_2018.tif
  format: null
  id: resource_b8a38d96
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_50_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_45_2018.tif
  format: null
  id: resource_7a55a92f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_45_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_40_2018.tif
  format: null
  id: resource_933bbee2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_40_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_35_2018.tif
  format: null
  id: resource_bac16493
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_35_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_30_2018.tif
  format: null
  id: resource_e80f91a5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_30_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_25_2018.tif
  format: null
  id: resource_34012133
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_25_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_20_2018.tif
  format: null
  id: resource_7db21263
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_20_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_1_2018.tif
  format: null
  id: resource_097a27d1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_1_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_15_2018.tif
  format: null
  id: resource_dd7c6f4c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_15_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_10_2018.tif
  format: null
  id: resource_a60b12a4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_10_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2018
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2018/BES/bes_f_0_2018.tif
  format: null
  id: resource_464e64ec
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_0_2018.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_80_2017.tif
  format: null
  id: resource_e58f7aab
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_75_2017.tif
  format: null
  id: resource_59b44c58
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_70_2017.tif
  format: null
  id: resource_6fa6feef
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_65_2017.tif
  format: null
  id: resource_b34f9131
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_60_2017.tif
  format: null
  id: resource_cfea8f80
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_5_2017.tif
  format: null
  id: resource_879ea337
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_55_2017.tif
  format: null
  id: resource_8306319f
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_50_2017.tif
  format: null
  id: resource_6c63075c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_45_2017.tif
  format: null
  id: resource_871c0780
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_40_2017.tif
  format: null
  id: resource_34ce17f6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_35_2017.tif
  format: null
  id: resource_82f8080a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_30_2017.tif
  format: null
  id: resource_aec64982
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_25_2017.tif
  format: null
  id: resource_df498972
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_20_2017.tif
  format: null
  id: resource_198c6356
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_1_2017.tif
  format: null
  id: resource_ddccc59a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_15_2017.tif
  format: null
  id: resource_d52b304e
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_10_2017.tif
  format: null
  id: resource_28ea6d11
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_m_0_2017.tif
  format: null
  id: resource_1dff1697
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_80_2017.tif
  format: null
  id: resource_c7317c19
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_80_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_75_2017.tif
  format: null
  id: resource_83ed48d5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_75_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_70_2017.tif
  format: null
  id: resource_40fc70bf
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_70_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_65_2017.tif
  format: null
  id: resource_9e9e80c9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_65_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_60_2017.tif
  format: null
  id: resource_033e5208
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_60_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_5_2017.tif
  format: null
  id: resource_668290ec
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_5_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_55_2017.tif
  format: null
  id: resource_dec254e3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_55_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_50_2017.tif
  format: null
  id: resource_64eef941
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_50_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_45_2017.tif
  format: null
  id: resource_1bf04ebb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_45_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_40_2017.tif
  format: null
  id: resource_d11a4f02
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_40_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_35_2017.tif
  format: null
  id: resource_cf71bb21
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_35_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_30_2017.tif
  format: null
  id: resource_f8ad89ec
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_30_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_25_2017.tif
  format: null
  id: resource_ed25207a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_25_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_20_2017.tif
  format: null
  id: resource_049634b9
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_20_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_1_2017.tif
  format: null
  id: resource_efe5d4b6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_1_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_15_2017.tif
  format: null
  id: resource_838dc79a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_15_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_10_2017.tif
  format: null
  id: resource_6965d541
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_10_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2017
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2017/BES/bes_f_0_2017.tif
  format: null
  id: resource_8aad69f4
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_0_2017.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_80_2016.tif
  format: null
  id: resource_8d2340c2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_75_2016.tif
  format: null
  id: resource_9be15301
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_70_2016.tif
  format: null
  id: resource_4657ede1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_65_2016.tif
  format: null
  id: resource_ba648abe
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_60_2016.tif
  format: null
  id: resource_f27294ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_5_2016.tif
  format: null
  id: resource_f8dea0e2
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_55_2016.tif
  format: null
  id: resource_1def0b6c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_50_2016.tif
  format: null
  id: resource_e2faf95c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_45_2016.tif
  format: null
  id: resource_5cee0a4d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_40_2016.tif
  format: null
  id: resource_f0ef702a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_35_2016.tif
  format: null
  id: resource_3c834885
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_30_2016.tif
  format: null
  id: resource_4e37966b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_25_2016.tif
  format: null
  id: resource_73a75fe5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_20_2016.tif
  format: null
  id: resource_def4c8eb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_1_2016.tif
  format: null
  id: resource_8eb6cfac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_15_2016.tif
  format: null
  id: resource_9ae1fa93
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_10_2016.tif
  format: null
  id: resource_2ef98bb5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_m_0_2016.tif
  format: null
  id: resource_7bf057ec
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_m_0_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_80_2016.tif
  format: null
  id: resource_9aac58d1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_80_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_75_2016.tif
  format: null
  id: resource_44bf2644
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_75_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_70_2016.tif
  format: null
  id: resource_1724ebcc
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_70_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_65_2016.tif
  format: null
  id: resource_98b2a775
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_65_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_60_2016.tif
  format: null
  id: resource_f58bd2c3
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_60_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_5_2016.tif
  format: null
  id: resource_f2df06c5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_5_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_55_2016.tif
  format: null
  id: resource_76a520ba
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_55_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_50_2016.tif
  format: null
  id: resource_80ea57b5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_50_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_45_2016.tif
  format: null
  id: resource_23a4c53d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_45_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_40_2016.tif
  format: null
  id: resource_3ee21d4a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_40_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_35_2016.tif
  format: null
  id: resource_9b91a2a7
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_35_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_30_2016.tif
  format: null
  id: resource_b44ddb0c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_30_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_25_2016.tif
  format: null
  id: resource_b7ef8b86
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_25_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_20_2016.tif
  format: null
  id: resource_49b02158
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_20_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_1_2016.tif
  format: null
  id: resource_c0ebbb2b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_1_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_15_2016.tif
  format: null
  id: resource_95d98ec8
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_15_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_10_2016.tif
  format: null
  id: resource_bb06ed7c
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_10_2016.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bonaire, Sint Eustatius and Saba 100m Age structures in 2016
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2000_2020/2016/BES/bes_f_0_2016.tif
  format: null
  id: resource_73ad0a7b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bes_f_0_2016.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bes_worldpop_bonairesinteustatiussabaa_2000
spatial:
  bbox: null
  centroid: null
  countries:
  - BES
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2020-12-31'
  start: '2000-01-01'
temporal_resolution: null
title: Bonaire, Sint Eustatius and Saba - Age and gender structures
version: null
vulnerability: null
---
