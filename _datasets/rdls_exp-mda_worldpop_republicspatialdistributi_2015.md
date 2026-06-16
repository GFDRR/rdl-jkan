---
attributions: []
catalog: Humanitarian Data Exchange
contact_point:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-mda
creator:
  affiliation: null
  email: null
  name: WorldPop
  url: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-mda
dataset_id: rdls_exp-mda_worldpop_republicspatialdistributi_2015
description: 'Estimates, total number of people per grid-cell. The dataset is available
  to download in Geotiff format at a resolution of 3 arc (approximately 100m at the
  equator). The projection is Geographic Coordinate System, WGS84. The units are number
  of people per pixel. The mapping approach is Random Forest-based dasymetric redistribution.
  More information can be found in the Release Statement Please note that these data
  represent 2025 Alpha release versions, constructed in September 2025. [Source: This
  metadata record was automatically extracted from the Humanitarian Data Exchange
  (HDX); Original dataset: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-mda]'
details: Disclaimer:The dataset currently represents an alpha version (R2025A) product
  and may change over the coming year as improvements are made. Data for earlier dates
  is available directly from WorldPop Bondarenko M., Priyatikanto R., Tejedor-Garavito
  N., Zhang W., McKeen T., Cunningham A., Woods T., Hilton J., Cihan D., Nosatiuk
  B., Brinkhoff T., Tatem A., Sorichetta A.. 2025 Constrained estimates of 2015-2030
  total number of people per grid square at a resolution of 3 arc (approximately 100m
  at the equator) R2025A version v1. Global Demographic Data Project - Funded by The
  Bill and Melinda Gates Foundation (INV-045237). WorldPop - School of Geography and
  Environmental Science, University of Southampton. DOI:10.5258/SOTON/WP00839
exposure:
- asset_type:
    description: Gridded population estimates at 100m and 1km resolution for Republic
      of Moldova (2015-2030)
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
  description: Gridded population estimates derived from census data and geospatial
    covariates using Random Forest-based dasymetric redistribution methodology. Data
    produced at 100m and 1km spatial resolutions for annual snapshots from 2015-2030
    in WGS84 geographic coordinate system.
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
- href: https://data.humdata.org/dataset/worldpop-population-counts-2015-2030-mda
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
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/MDA/v1/100m/constrained/mda_pop_2015_CN_100m_R2025A_v1.tif
  format: null
  id: resource_98cb51be
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2015_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2015)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2015/MDA/v1/1km_ua/constrained/mda_pop_2015_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_ee260ffd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2015_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/MDA/v1/100m/constrained/mda_pop_2016_CN_100m_R2025A_v1.tif
  format: null
  id: resource_f8052bea
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2016_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2016)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2016/MDA/v1/1km_ua/constrained/mda_pop_2016_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_e9994b82
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2016_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/MDA/v1/100m/constrained/mda_pop_2017_CN_100m_R2025A_v1.tif
  format: null
  id: resource_76418813
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2017_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2017)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2017/MDA/v1/1km_ua/constrained/mda_pop_2017_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_1bdfbac1
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2017_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/MDA/v1/100m/constrained/mda_pop_2018_CN_100m_R2025A_v1.tif
  format: null
  id: resource_d57a55be
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2018_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2018)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2018/MDA/v1/1km_ua/constrained/mda_pop_2018_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_0ac60957
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2018_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/MDA/v1/100m/constrained/mda_pop_2019_CN_100m_R2025A_v1.tif
  format: null
  id: resource_5dc4c727
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2019_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2019)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2019/MDA/v1/1km_ua/constrained/mda_pop_2019_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_bc3db771
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2019_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/MDA/v1/100m/constrained/mda_pop_2020_CN_100m_R2025A_v1.tif
  format: null
  id: resource_a3cde8f6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2020_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2020)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2020/MDA/v1/1km_ua/constrained/mda_pop_2020_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f83e1e15
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2020_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/MDA/v1/100m/constrained/mda_pop_2021_CN_100m_R2025A_v1.tif
  format: null
  id: resource_efb09cd6
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2021_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2021)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2021/MDA/v1/1km_ua/constrained/mda_pop_2021_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_8a6e7def
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2021_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/MDA/v1/100m/constrained/mda_pop_2022_CN_100m_R2025A_v1.tif
  format: null
  id: resource_cb388f45
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2022_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2022)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2022/MDA/v1/1km_ua/constrained/mda_pop_2022_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_0c61eedd
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2022_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/MDA/v1/100m/constrained/mda_pop_2023_CN_100m_R2025A_v1.tif
  format: null
  id: resource_b8547831
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2023_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2023)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2023/MDA/v1/1km_ua/constrained/mda_pop_2023_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_c225a126
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2023_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/MDA/v1/100m/constrained/mda_pop_2024_CN_100m_R2025A_v1.tif
  format: null
  id: resource_26418a30
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2024_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2024)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2024/MDA/v1/1km_ua/constrained/mda_pop_2024_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_2e49468b
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2024_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/MDA/v1/100m/constrained/mda_pop_2025_CN_100m_R2025A_v1.tif
  format: null
  id: resource_aec1d104
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2025_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2025)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2025/MDA/v1/1km_ua/constrained/mda_pop_2025_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_bd8c1a61
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2025_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/MDA/v1/100m/constrained/mda_pop_2026_CN_100m_R2025A_v1.tif
  format: null
  id: resource_97fb5560
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2026_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2026)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2026/MDA/v1/1km_ua/constrained/mda_pop_2026_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_c8ebe173
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2026_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/MDA/v1/100m/constrained/mda_pop_2027_CN_100m_R2025A_v1.tif
  format: null
  id: resource_0858fe79
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2027_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2027)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2027/MDA/v1/1km_ua/constrained/mda_pop_2027_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_d3b0dddb
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2027_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/MDA/v1/100m/constrained/mda_pop_2028_CN_100m_R2025A_v1.tif
  format: null
  id: resource_dcba7958
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2028_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2028)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2028/MDA/v1/1km_ua/constrained/mda_pop_2028_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_f3a0cc9a
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2028_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/MDA/v1/100m/constrained/mda_pop_2029_CN_100m_R2025A_v1.tif
  format: null
  id: resource_04f69b6d
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2029_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2029)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2029/MDA/v1/1km_ua/constrained/mda_pop_2029_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_cc8dd4e5
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2029_cn_1km.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (100m resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/MDA/v1/100m/constrained/mda_pop_2030_CN_100m_R2025A_v1.tif
  format: null
  id: resource_300cd1ac
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2030_cn_100m.tif
- access_url: null
  baseline_period: null
  climate: null
  conforms_to: null
  coordinate_system: null
  description: Republic of Moldova - Spatial Distribution of Population (2015-2030)
    (Individual population counts (1km resolution) for 2030)
  download_url: https://data.worldpop.org/GIS/Population/Global_2015_2030/R2025A/2030/MDA/v1/1km_ua/constrained/mda_pop_2030_CN_1km_R2025A_UA_v1.tif
  format: null
  id: resource_d7213044
  media_type: image/tiff;application=geotiff
  spatial: null
  spatial_aggregation: null
  spatial_resolution: null
  temporal: null
  temporal_resolution: null
  title: mda_pop_2030_cn_1km.tif
risk_data_type:
- exposure
schema: rdls-10
slug: rdls_exp-mda_worldpop_republicspatialdistributi_2015
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
title: Republic of Moldova - Spatial Distribution of Population (2015-2030)
version: null
vulnerability: null
---
