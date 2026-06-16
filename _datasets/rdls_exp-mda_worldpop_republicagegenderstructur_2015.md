---
attributions:
- entity:
    affiliation: null
    email: null
    name: WorldPop Global 2015-2030 R2025A
    url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-mda
  id: attribution_1
  role: collaborator
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-mda
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-mda
dataset_id: rdls_exp-mda_worldpop_republicagegenderstructur_2015
description: 'Estimates of total number of people per grid square broken down by gender
  and age groupings (including 0-1 and by 5-year up to 90+) for Republic of Moldova,
  R2025A version v1. The dataset is available to download in Geotiff format at a resolution
  of 3 arc (approximately 100m at the equator). The projection is Geographic Coordinate
  System, WGS84. The units are estimated number of male, female or both in each age
  group per grid square. More information can be found in the Release Statement Please
  note that these data represent 2025 Alpha release versions, constructed in September
  2025 File Descriptions: {iso} {gender} {age group} {year} {type} {resolution}.tif
  iso Three-letter country code gender m = male, f= female, t = both genders age group
  00 = age group 0 to 12 months 01 = age group 1 to 4 years 05 = age group 5 to 9
  years 90 = age 90 years and over year Year that the population represents type CN
  = Constrained resolution Resolution of the data e.q. 100m = 3 arc (approximately
  100m at the equator). [Source: This metadata record was automatically extracted
  from the Humanitarian Data Exchange (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-mda]'
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
    description: "Gridded population estimates for Republic of Moldova disaggregated\
      \ by gender and 5-year age groups (0-1 and up to 90+) at 100m and 1km resolution\
      \ for years 2015\xE2\u20AC\u201C2030"
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
  description: Age- and gender-disaggregated gridded population estimates for Moldova
    were produced by WorldPop using the R2025A modelling framework, which integrates
    national census data, demographic surveys, and ancillary geospatial covariates
    (e.g., land cover, building footprints) via a random forest dasymetric mapping
    methodology. Outputs are provided as GeoTIFF rasters at 100m and 1km resolution
    in WGS84, covering annual time steps from 2015 to 2030, and are intended for use
    in humanitarian planning, disaster risk assessment, and exposure modelling.
  sources:
  - id: source_1
    license: null
    name: WorldPop Global 2015-2030 R2025A
    risk_data_type:
    - exposure
    type: model
    url: null
    used_in: exposure
links:
- href: https://docs.riskdatalibrary.org/en/1__0__0/rdls_schema.json
  rel: describedby
- href: https://data.humdata.org/dataset/worldpop-age-and-gender-structures-2015-2030-mda
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
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2015/MDA/v1/100m/mda_agesex_structures_2015_CN_100m_R2025A_v1.zip
  format: null
  id: resource_0a714d63
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2015_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2015/MDA/v1/1km_ua/mda_agesex_structures_2015_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_a072b49c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2015_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2016/MDA/v1/100m/mda_agesex_structures_2016_CN_100m_R2025A_v1.zip
  format: null
  id: resource_86997539
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2016_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2016/MDA/v1/1km_ua/mda_agesex_structures_2016_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_69b098a3
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2016_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2017/MDA/v1/100m/mda_agesex_structures_2017_CN_100m_R2025A_v1.zip
  format: null
  id: resource_4da6321e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2017_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2017/MDA/v1/1km_ua/mda_agesex_structures_2017_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_58597059
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2017_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2018/MDA/v1/100m/mda_agesex_structures_2018_CN_100m_R2025A_v1.zip
  format: null
  id: resource_6c1199f8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2018_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2018/MDA/v1/1km_ua/mda_agesex_structures_2018_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_da6a5e71
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2018_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2019/MDA/v1/100m/mda_agesex_structures_2019_CN_100m_R2025A_v1.zip
  format: null
  id: resource_318a685a
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2019_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2019/MDA/v1/1km_ua/mda_agesex_structures_2019_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_1c649d19
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2019_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2020/MDA/v1/100m/mda_agesex_structures_2020_CN_100m_R2025A_v1.zip
  format: null
  id: resource_acd45fdb
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2020_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2020/MDA/v1/1km_ua/mda_agesex_structures_2020_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_db7adda1
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2020_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2021/MDA/v1/100m/mda_agesex_structures_2021_CN_100m_R2025A_v1.zip
  format: null
  id: resource_d192a4a6
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2021_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2021/MDA/v1/1km_ua/mda_agesex_structures_2021_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_9f9f367f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2021_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2022/MDA/v1/100m/mda_agesex_structures_2022_CN_100m_R2025A_v1.zip
  format: null
  id: resource_821f02d9
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2022_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2022/MDA/v1/1km_ua/mda_agesex_structures_2022_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_500b30e8
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2022_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2023/MDA/v1/100m/mda_agesex_structures_2023_CN_100m_R2025A_v1.zip
  format: null
  id: resource_5eb9cd20
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2023_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2023/MDA/v1/1km_ua/mda_agesex_structures_2023_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_c613701f
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2023_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2024/MDA/v1/100m/mda_agesex_structures_2024_CN_100m_R2025A_v1.zip
  format: null
  id: resource_ff53b678
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2024_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2024/MDA/v1/1km_ua/mda_agesex_structures_2024_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_0bac80c4
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2024_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2025/MDA/v1/100m/mda_agesex_structures_2025_CN_100m_R2025A_v1.zip
  format: null
  id: resource_82b68c0e
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2025_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2025/MDA/v1/1km_ua/mda_agesex_structures_2025_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_ba644737
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2025_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2026/MDA/v1/100m/mda_agesex_structures_2026_CN_100m_R2025A_v1.zip
  format: null
  id: resource_db9cb6da
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2026_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2026/MDA/v1/1km_ua/mda_agesex_structures_2026_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_6dc2212c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2026_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2027/MDA/v1/100m/mda_agesex_structures_2027_CN_100m_R2025A_v1.zip
  format: null
  id: resource_37ade2ec
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2027_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2027/MDA/v1/1km_ua/mda_agesex_structures_2027_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_6276d093
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2027_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2028/MDA/v1/100m/mda_agesex_structures_2028_CN_100m_R2025A_v1.zip
  format: null
  id: resource_ceb85d37
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2028_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2028/MDA/v1/1km_ua/mda_agesex_structures_2028_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_1220d411
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2028_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2029/MDA/v1/100m/mda_agesex_structures_2029_CN_100m_R2025A_v1.zip
  format: null
  id: resource_c7d5033c
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2029_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2029/MDA/v1/1km_ua/mda_agesex_structures_2029_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_69661a39
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2029_cn_1km.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (100m resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2030/MDA/v1/100m/mda_agesex_structures_2030_CN_100m_R2025A_v1.zip
  format: null
  id: resource_e2ab1905
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2030_cn_100m.zip
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Age and Gender Structures (2015-2030) (Individual
    age and gender structures (1km resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/AgeSex_structures/Global_2015_2030/R2025A/2030/MDA/v1/1km_ua/mda_agesex_structures_2030_CN_1km_R2025A_UA_v1.zip
  format: null
  id: resource_852efad7
  media_type: application/zip
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_agegender_structures_2030_cn_1km.zip
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mda_worldpop_republicagegenderstructur_2015
spatial:
  bbox: null
  centroid: null
  countries:
  - MDA
  gazetteer_entries: []
  scale: national
spatial_resolution: null
temporal:
  central_year: null
  duration: null
  end: '2030-01-01'
  start: '2015-01-01'
temporal_resolution: null
title: Republic of Moldova - Age and Gender Structures (2015-2030)
version: null
vulnerability: null
---
