---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-mnp
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-mnp
dataset_id: rdls_exp-mnp_worldpop_northernmarianaislandsage_2015
description: 'Estimates of total number of people per grid square broken down by gender
  and age groupings (including 0-1 and by 5-year up to 90+) for Northern Mariana Islands
  (USA), R2025A version v1. The dataset is available to download in Geotiff format
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
  extracted from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-mnp]'
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
    description: Gridded population estimates disaggregated by age group (0-1, 5-year
      intervals to 90+) and gender for Northern Mariana Islands at 100m and 1km resolution
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
  description: WorldPop R2025A version integrates multiple demographic sources (census,
    surveys) with spatial modeling to produce gridded population estimates disaggregated
    by age group and gender at 100m and 1km resolution for Northern Mariana Islands
    across 2015-2030, providing baseline exposure data for disaster risk assessment.
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-mnp
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
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2015/MNP/v1/100m/mnp_agesex_structures_2015_CN_100m_R2025A_v1.zip
  format: null
  id: resource_04423aa1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2015_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2015/MNP/v1/1km_ua/mnp_agesex_structures_2015_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_152408a6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2015_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2016/MNP/v1/100m/mnp_agesex_structures_2016_CN_100m_R2025A_v1.zip
  format: null
  id: resource_54804920
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2016_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2016/MNP/v1/1km_ua/mnp_agesex_structures_2016_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_27015018
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2016_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2017/MNP/v1/100m/mnp_agesex_structures_2017_CN_100m_R2025A_v1.zip
  format: null
  id: resource_a0f820f8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2017_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2017/MNP/v1/1km_ua/mnp_agesex_structures_2017_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_cc5457dd
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2017_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2018/MNP/v1/100m/mnp_agesex_structures_2018_CN_100m_R2025A_v1.zip
  format: null
  id: resource_426e613b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2018_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2018/MNP/v1/1km_ua/mnp_agesex_structures_2018_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_fa010012
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2018_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2019/MNP/v1/100m/mnp_agesex_structures_2019_CN_100m_R2025A_v1.zip
  format: null
  id: resource_f6c823c8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2019_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2019/MNP/v1/1km_ua/mnp_agesex_structures_2019_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_47b8d082
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2019_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2020/MNP/v1/100m/mnp_agesex_structures_2020_CN_100m_R2025A_v1.zip
  format: null
  id: resource_8f5061e6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2020_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2020/MNP/v1/1km_ua/mnp_agesex_structures_2020_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_afe3594b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2020_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2021/MNP/v1/100m/mnp_agesex_structures_2021_CN_100m_R2025A_v1.zip
  format: null
  id: resource_b5ba5b1d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2021_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2021/MNP/v1/1km_ua/mnp_agesex_structures_2021_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_0fd09c29
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2021_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2022/MNP/v1/100m/mnp_agesex_structures_2022_CN_100m_R2025A_v1.zip
  format: null
  id: resource_5c54ef7f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2022_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2022/MNP/v1/1km_ua/mnp_agesex_structures_2022_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_173b42d8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2022_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2023/MNP/v1/100m/mnp_agesex_structures_2023_CN_100m_R2025A_v1.zip
  format: null
  id: resource_7c7b5396
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2023_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2023/MNP/v1/1km_ua/mnp_agesex_structures_2023_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_c2145297
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2023_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2024/MNP/v1/100m/mnp_agesex_structures_2024_CN_100m_R2025A_v1.zip
  format: null
  id: resource_0c25e206
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2024_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2024/MNP/v1/1km_ua/mnp_agesex_structures_2024_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_318c9e57
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2024_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2025/MNP/v1/100m/mnp_agesex_structures_2025_CN_100m_R2025A_v1.zip
  format: null
  id: resource_fd7f6fde
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2025_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2025/MNP/v1/1km_ua/mnp_agesex_structures_2025_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_1b3987a4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2025_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2026/MNP/v1/100m/mnp_agesex_structures_2026_CN_100m_R2025A_v1.zip
  format: null
  id: resource_076203fa
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2026_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2026/MNP/v1/1km_ua/mnp_agesex_structures_2026_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_72023840
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2026_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2027/MNP/v1/100m/mnp_agesex_structures_2027_CN_100m_R2025A_v1.zip
  format: null
  id: resource_79a59e6e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2027_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2027/MNP/v1/1km_ua/mnp_agesex_structures_2027_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_a4213593
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2027_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2028/MNP/v1/100m/mnp_agesex_structures_2028_CN_100m_R2025A_v1.zip
  format: null
  id: resource_c7f8bdb7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2028_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2028/MNP/v1/1km_ua/mnp_agesex_structures_2028_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_1867f523
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2028_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2029/MNP/v1/100m/mnp_agesex_structures_2029_CN_100m_R2025A_v1.zip
  format: null
  id: resource_ce58a5bb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2029_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2029/MNP/v1/1km_ua/mnp_agesex_structures_2029_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_eb5328f5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2029_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2030/MNP/v1/100m/mnp_agesex_structures_2030_CN_100m_R2025A_v1.zip
  format: null
  id: resource_b000c9f7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2030_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Northern Mariana Islands - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2030/MNP/v1/1km_ua/mnp_agesex_structures_2030_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_9f20ce35
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mnp_agegender_structures_2030_cn_1km.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mnp_worldpop_northernmarianaislandsage_2015
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
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: Northern Mariana Islands - Age and Gender Structures (2015-2030)
version: null
vulnerability: null
---
