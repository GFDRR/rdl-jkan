---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-bol
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-bol
dataset_id: rdls_exp-bol_worldpop_plurinationalstateagegend_2015
description: 'Estimates of total number of people per grid square broken down by gender
  and age groupings (including 0-1 and by 5-year up to 90+) for Bolivia (Plurinational
  State of), R2025A version v1. The dataset is available to download in Geotiff format
  at a resolution of 3 arc (approximately 100m at the equator). The projection is
  Geographic Coordinate System, WGS84. The units are estimated number of male, female
  or both in each age group per grid square. More information can be found in the
  Release Statement Please note that these data represent 2025 Alpha release versions,
  constructed in September 2025 File Descriptions: {iso} {gender} {age group} {year}
  {type} {resolution}.tif iso Three-letter country code gender m = male, f= female,
  t = both genders age group 00 = age group 0 to 12 months 01 = age group 1 to 4 years
  05 = age group 5 to 9 years 90 = age 90 years and over year Year that the population
  represents type CN = Constrained resolution Resolution of the data e.q. 100m = 3
  arc (approximately 100m at the equator). [Source: This metadata record was automatically
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-bol]'
details: Data for earlier dates is available directly from WorldPop Bondarenko M.,
  Priyatikanto R., Tejedor-Garavito N., Zhang W., McKeen T., Cunningham A., Woods
  T., Hilton J., Cihan D., Nosatiuk B., Brinkhoff T., Tatem A., Sorichetta A.. 2025.
  Estimates of 2015-2030 total number of people per grid square broken down by gender
  and age groupings at a resolution of 3 arc (approximately 100m at the equator) R2025A
  version v1. Global Demographic Data Project - Funded by The Bill and Melinda Gates
  Foundation (INV-045237). WorldPop - School of Geography and Environmental Science,
  University of Southampton. DOI:10.5258/SOTON/WP00841
exposure:
- asset_type:
    description: Gridded population estimates disaggregated by age groups (0-1, 5-year
      intervals to 90+) and gender for Bolivia 2015-2030
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
  description: WorldPop R2025A version provides spatially disaggregated population
    estimates for Bolivia by integrating census data, survey information, and geospatial
    modeling to produce gridded population counts stratified by age group and gender
    at 100m and 1km resolutions for the period 2015-2030.
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-bol
  rel: source
loss: null
project: null
publisher:
  affiliation: null
  email: null
  name: Humanitarian Data Exchange (HDX)
  url: https://data.humdata.org/
purpose: null
referenced_by:
- author_names: null
  date_published: null
  doi: null
  id: reference_1
  name: Methodology documentation
  url: https://data.worldpop.org/repo/prj/Global_2015_2030/R2025A/doc/Global2_Release_Statement_R2025A_v1.pdf
resources:
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2015/BOL/v1/100m/bol_agesex_structures_2015_CN_100m_R2025A_v1.zip
  format: null
  id: resource_ec03d900
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2015_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2015/BOL/v1/1km_ua/bol_agesex_structures_2015_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_d6e061b5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2015_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2016/BOL/v1/100m/bol_agesex_structures_2016_CN_100m_R2025A_v1.zip
  format: null
  id: resource_2d67c219
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2016_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2016/BOL/v1/1km_ua/bol_agesex_structures_2016_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_f67a519e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2016_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2017/BOL/v1/100m/bol_agesex_structures_2017_CN_100m_R2025A_v1.zip
  format: null
  id: resource_8131e8de
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2017_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2017/BOL/v1/1km_ua/bol_agesex_structures_2017_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_033714b9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2017_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2018/BOL/v1/100m/bol_agesex_structures_2018_CN_100m_R2025A_v1.zip
  format: null
  id: resource_0f342b10
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2018_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2018/BOL/v1/1km_ua/bol_agesex_structures_2018_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_e7f104ed
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2018_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2019/BOL/v1/100m/bol_agesex_structures_2019_CN_100m_R2025A_v1.zip
  format: null
  id: resource_9ba059a9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2019_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2019/BOL/v1/1km_ua/bol_agesex_structures_2019_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_e305631c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2019_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2020/BOL/v1/100m/bol_agesex_structures_2020_CN_100m_R2025A_v1.zip
  format: null
  id: resource_45d01277
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2020_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2020/BOL/v1/1km_ua/bol_agesex_structures_2020_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_62db1bb8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2020_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2021/BOL/v1/100m/bol_agesex_structures_2021_CN_100m_R2025A_v1.zip
  format: null
  id: resource_e47c2247
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2021_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2021/BOL/v1/1km_ua/bol_agesex_structures_2021_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_7f22b236
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2021_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2022/BOL/v1/100m/bol_agesex_structures_2022_CN_100m_R2025A_v1.zip
  format: null
  id: resource_1e933f8e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2022_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2022/BOL/v1/1km_ua/bol_agesex_structures_2022_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_c777e149
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2022_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2023/BOL/v1/100m/bol_agesex_structures_2023_CN_100m_R2025A_v1.zip
  format: null
  id: resource_71083fff
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2023_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2023/BOL/v1/1km_ua/bol_agesex_structures_2023_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_72c6673a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2023_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2024/BOL/v1/100m/bol_agesex_structures_2024_CN_100m_R2025A_v1.zip
  format: null
  id: resource_ff4ca495
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2024_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2024/BOL/v1/1km_ua/bol_agesex_structures_2024_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_65454bbd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2024_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2025/BOL/v1/100m/bol_agesex_structures_2025_CN_100m_R2025A_v1.zip
  format: null
  id: resource_8a9ec35b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2025_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2025/BOL/v1/1km_ua/bol_agesex_structures_2025_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_731f57f1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2025_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2026/BOL/v1/100m/bol_agesex_structures_2026_CN_100m_R2025A_v1.zip
  format: null
  id: resource_8941b8a1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2026_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2026/BOL/v1/1km_ua/bol_agesex_structures_2026_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_a96090c0
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2026_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2027/BOL/v1/100m/bol_agesex_structures_2027_CN_100m_R2025A_v1.zip
  format: null
  id: resource_ddafaaa9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2027_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2027/BOL/v1/1km_ua/bol_agesex_structures_2027_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_6a7367e7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2027_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2028/BOL/v1/100m/bol_agesex_structures_2028_CN_100m_R2025A_v1.zip
  format: null
  id: resource_8be03d7b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2028_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2028/BOL/v1/1km_ua/bol_agesex_structures_2028_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_c34f4f37
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2028_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2029/BOL/v1/100m/bol_agesex_structures_2029_CN_100m_R2025A_v1.zip
  format: null
  id: resource_35488a79
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2029_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2029/BOL/v1/1km_ua/bol_agesex_structures_2029_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_0ba949d3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2029_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (100m resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2030/BOL/v1/100m/bol_agesex_structures_2030_CN_100m_R2025A_v1.zip
  format: null
  id: resource_6e12ff56
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2030_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
    (Individual age and gender structures (1km resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2030/BOL/v1/1km_ua/bol_agesex_structures_2030_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_97f11305
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: bol_agegender_structures_2030_cn_1km.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-bol_worldpop_plurinationalstateagegend_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - BOL
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: Bolivia (Plurinational State of) - Age and Gender Structures (2015-2030)
version: null
vulnerability: null
---
