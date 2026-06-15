---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-zmb
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-zmb
dataset_id: rdls_exp-zmb_worldpop_agegenderstructures201520_2015
description: 'Estimates of total number of people per grid square broken down by gender
  and age groupings (including 0-1 and by 5-year up to 90+) for Zambia, R2025A version
  v1. The dataset is available to download in Geotiff format at a resolution of 3
  arc (approximately 100m at the equator). The projection is Geographic Coordinate
  System, WGS84. The units are estimated number of male, female or both in each age
  group per grid square. More information can be found in the Release Statement Please
  note that these data represent 2025 Alpha release versions, constructed in September
  2025 File Descriptions: {iso} {gender} {age group} {year} {type} {resolution}.tif
  iso Three-letter country code gender m = male, f= female, t = both genders age group
  00 = age group 0 to 12 months 01 = age group 1 to 4 years 05 = age group 5 to 9
  years 90 = age 90 years and over year Year that the population represents type CN
  = Constrained resolution Resolution of the data e.q. 100m = 3 arc (approximately
  100m at the equator). [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-zmb]'
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
    description: Gridded population estimates disaggregated by gender and age groups
      (0-1, 5-year intervals to 90+) for Zambia at 100m and 1km resolution
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
  description: WorldPop Global 2015-2030 R2025A dataset provides modeled gridded population
    estimates for Zambia derived from multiple demographic and geospatial sources,
    disaggregated by gender and age cohorts at 100m and 1km spatial resolution in
    GeoTIFF format.
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
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-zmb
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
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2015/ZMB/v1/100m/zmb_agesex_structures_2015_CN_100m_R2025A_v1.zip
  format: null
  id: resource_fb9b5db3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2015_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2015/ZMB/v1/1km_ua/zmb_agesex_structures_2015_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_38c6a147
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2015_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2016/ZMB/v1/100m/zmb_agesex_structures_2016_CN_100m_R2025A_v1.zip
  format: null
  id: resource_fc8fae4b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2016_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2016/ZMB/v1/1km_ua/zmb_agesex_structures_2016_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_6ff21a6a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2016_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2017/ZMB/v1/100m/zmb_agesex_structures_2017_CN_100m_R2025A_v1.zip
  format: null
  id: resource_e8d41eb9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2017_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2017/ZMB/v1/1km_ua/zmb_agesex_structures_2017_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_ffc304a6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2017_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2018/ZMB/v1/100m/zmb_agesex_structures_2018_CN_100m_R2025A_v1.zip
  format: null
  id: resource_fdfe9cca
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2018_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2018/ZMB/v1/1km_ua/zmb_agesex_structures_2018_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_5a8456c7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2018_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2019/ZMB/v1/100m/zmb_agesex_structures_2019_CN_100m_R2025A_v1.zip
  format: null
  id: resource_65f66e7c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2019_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2019/ZMB/v1/1km_ua/zmb_agesex_structures_2019_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_9b1ddf5e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2019_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2020/ZMB/v1/100m/zmb_agesex_structures_2020_CN_100m_R2025A_v1.zip
  format: null
  id: resource_3025fe84
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2020_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2020/ZMB/v1/1km_ua/zmb_agesex_structures_2020_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_ee2eb4be
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2020_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2021/ZMB/v1/100m/zmb_agesex_structures_2021_CN_100m_R2025A_v1.zip
  format: null
  id: resource_7af211ae
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2021_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2021/ZMB/v1/1km_ua/zmb_agesex_structures_2021_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_b2eb6e8d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2021_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2022/ZMB/v1/100m/zmb_agesex_structures_2022_CN_100m_R2025A_v1.zip
  format: null
  id: resource_64d1db91
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2022_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2022/ZMB/v1/1km_ua/zmb_agesex_structures_2022_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_c02acba5
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2022_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2023/ZMB/v1/100m/zmb_agesex_structures_2023_CN_100m_R2025A_v1.zip
  format: null
  id: resource_acf8e155
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2023_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2023/ZMB/v1/1km_ua/zmb_agesex_structures_2023_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_a6358cb8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2023_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2024/ZMB/v1/100m/zmb_agesex_structures_2024_CN_100m_R2025A_v1.zip
  format: null
  id: resource_89b45c67
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2024_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2024/ZMB/v1/1km_ua/zmb_agesex_structures_2024_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_f7c0e53d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2024_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2025/ZMB/v1/100m/zmb_agesex_structures_2025_CN_100m_R2025A_v1.zip
  format: null
  id: resource_2d56a6ec
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2025_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2025/ZMB/v1/1km_ua/zmb_agesex_structures_2025_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_b6f9258e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2025_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2026/ZMB/v1/100m/zmb_agesex_structures_2026_CN_100m_R2025A_v1.zip
  format: null
  id: resource_ba125439
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2026_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2026/ZMB/v1/1km_ua/zmb_agesex_structures_2026_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_e6adfd7c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2026_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2027/ZMB/v1/100m/zmb_agesex_structures_2027_CN_100m_R2025A_v1.zip
  format: null
  id: resource_20acba39
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2027_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2027/ZMB/v1/1km_ua/zmb_agesex_structures_2027_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_9f9a7f95
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2027_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2028/ZMB/v1/100m/zmb_agesex_structures_2028_CN_100m_R2025A_v1.zip
  format: null
  id: resource_8e00300d
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2028_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2028/ZMB/v1/1km_ua/zmb_agesex_structures_2028_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_c66a7ec2
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2028_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2029/ZMB/v1/100m/zmb_agesex_structures_2029_CN_100m_R2025A_v1.zip
  format: null
  id: resource_bc1efb3a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2029_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2029/ZMB/v1/1km_ua/zmb_agesex_structures_2029_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_8e074fe4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2029_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (100m resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2030/ZMB/v1/100m/zmb_agesex_structures_2030_CN_100m_R2025A_v1.zip
  format: null
  id: resource_52578051
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2030_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Zambia - Age and Gender Structures (2015-2030) (Individual age and
    gender structures (1km resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2030/ZMB/v1/1km_ua/zmb_agesex_structures_2030_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_382be79b
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: zmb_agegender_structures_2030_cn_1km.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-zmb_worldpop_agegenderstructures201520_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - ZMB
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: Zambia - Age and Gender Structures (2015-2030)
version: null
vulnerability: null
---
